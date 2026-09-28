"""Maquetado navegable (HTML + Python/Flask). Datos ficticios en memoria. Ejecutar: python app.py"""
from datetime import date
from flask import Flask, render_template, request, redirect, url_for, flash, abort

app = Flask(__name__)
app.secret_key = "demo"
VET = "Dra. Ana Ríos"  # veterinaria ficticia con sesión iniciada
DB = {
    "pacientes": {
        1: dict(nombre="Luna", especie="Perro", raza="Caniche", nac="03/2019", tutor="M. Gómez", peso=6.8, activos=["Prednisolona 5 mg"]),
        2: dict(nombre="Toby", especie="Gato", raza="Común europeo", nac="08/2021", tutor="L. Pérez", peso=4.1, activos=[]),
    },
    "hist": {
        1: [dict(id=2, fecha="12/08/2026", sintomas="Picazón persistente", dx="Dermatitis alérgica", obs="Se inicia tratamiento.", peso=6.8, autor="Dra. Ana Ríos", editada=False, extra=[]),
            dict(id=1, fecha="02/05/2026", sintomas="Control anual", dx="Sin hallazgos", obs="Sin novedades.", peso=6.5, autor="Dr. Pablo Sosa", editada=False, extra=["Vacuna: Antirrábica (lote A123, vence 05/2027)"])],
        2: [],
    },
}
INTERACCIONES = {frozenset(("meloxicam", "prednisolona")): "Antiinflamatorio no esteroideo + corticoide: mayor riesgo de daño gastrointestinal. (Dato de ejemplo de la maqueta.)"}

@app.context_processor
def ctx():
    return dict(pacientes=DB["pacientes"], vet=VET, hoy=date.today().isoformat())

def pac(pid):
    if pid not in DB["pacientes"]: abort(404)
    return DB["pacientes"][pid]

def conflicto(pid, farmaco):
    nuevo = (farmaco.strip().lower().split() or [""])[0]
    for a in DB["pacientes"][pid]["activos"]:
        msg = INTERACCIONES.get(frozenset((nuevo, a.lower().split()[0])))
        if msg: return a, msg

@app.route("/")
def inicio(): return redirect(url_for("historial", pid=1))

@app.route("/buscar")
def buscar():
    q = request.args.get("q", "").strip().lower()
    for pid, p in DB["pacientes"].items():
        if q and q in p["nombre"].lower(): return redirect(url_for("historial", pid=pid))
    flash("No se encontró ningún paciente con ese nombre. Revisá la ortografía o elegí uno de la lista.", "err")
    return redirect(request.referrer or url_for("inicio"))

@app.route("/paciente/<int:pid>")
def historial(pid):
    return render_template("historial.html", pid=pid, p=pac(pid), hist=DB["hist"][pid])

@app.route("/paciente/<int:pid>/consulta/nueva", methods=["GET", "POST"])
def nueva_consulta(pid):
    p = pac(pid); err = {}
    v = request.form if request.method == "POST" else {"fecha": date.today().isoformat()}
    if request.method == "POST":
        if not v.get("fecha"): err["fecha"] = "Indicá la fecha de la consulta."
        elif v["fecha"] > date.today().isoformat(): err["fecha"] = "La fecha no puede ser posterior a hoy."
        try:
            peso = float(v.get("peso", "").replace(",", "."))
            if peso <= 0: raise ValueError
        except ValueError:
            err["peso"] = "El peso debe ser un número mayor a 0 (en kg)."
        if not v.get("sintomas", "").strip(): err["sintomas"] = "Describí los síntomas detectados."
        if not v.get("dx", "").strip(): err["dx"] = "Ingresá el diagnóstico preliminar."
        if not err:
            extra = []
            if v.get("vacuna"): extra.append(f"Vacuna: {v['vacuna']} (lote {v.get('lote') or '—'}, vence {v.get('vence') or '—'})")
            if v.get("patologias"): extra.append(f"Patologías: {v['patologias']}")
            if v.get("procedimientos"): extra.append(f"Procedimientos: {v['procedimientos']}")
            nid = max([e["id"] for e in DB["hist"][pid]] or [0]) + 1
            DB["hist"][pid].insert(0, dict(id=nid, fecha="/".join(reversed(v["fecha"].split("-"))), sintomas=v["sintomas"], dx=v["dx"],
                                           obs=v.get("obs", ""), peso=peso, autor=VET, editada=False, extra=extra))
            p["peso"] = peso
            flash("Consulta guardada. El historial y el peso vigente se actualizaron.", "ok")
            return redirect(url_for("historial", pid=pid))
    return render_template("consulta.html", pid=pid, p=p, v=v, errores=err)

@app.route("/paciente/<int:pid>/entrada/<int:eid>/editar", methods=["GET", "POST"])
def editar(pid, eid):
    p = pac(pid); e = next((x for x in DB["hist"][pid] if x["id"] == eid), None)
    if e is None: abort(404)
    if e["autor"] != VET:
        flash("Solo el autor de la entrada puede editarla.", "err"); return redirect(url_for("historial", pid=pid))
    err = {}
    if request.method == "POST":
        obs = request.form.get("obs", "").strip()
        if not obs: err["obs"] = "La observación no puede quedar vacía."
        else:
            e["obs"], e["editada"] = obs, True
            flash("Entrada actualizada. Quedó marcada como modificada en el historial.", "ok")
            return redirect(url_for("historial", pid=pid))
    return render_template("editar.html", pid=pid, p=p, e=e, errores=err, obs=request.form.get("obs", e["obs"]))

@app.route("/paciente/<int:pid>/prescribir", methods=["GET", "POST"])
def prescribir(pid):
    p = pac(pid); v = request.form if request.method == "POST" else {}; err = {}; alerta = None
    if request.method == "POST":
        if v.get("accion") == "cancelar":
            flash("Prescripción cancelada. No se registró ningún cambio.", "ok"); return redirect(url_for("historial", pid=pid))
        if not v.get("farmaco", "").strip(): err["farmaco"] = "Indicá el fármaco o suplemento."
        if not v.get("dosis", "").strip(): err["dosis"] = "Indicá la dosis."
        if v.get("vigencia") and v["vigencia"] < date.today().isoformat(): err["vigencia"] = "La vigencia no puede estar vencida."
        if not err:
            c = conflicto(pid, v["farmaco"])
            if c and v.get("accion") != "continuar": alerta = c
            elif c and not v.get("justificacion", "").strip():
                alerta = c; err["justificacion"] = "Escribí la justificación para continuar."
            else:
                p["activos"].append(f"{v['farmaco'].strip()} {v['dosis'].strip()}")
                flash("Prescripción registrada en el plan de tratamiento.", "ok"); return redirect(url_for("historial", pid=pid))
    return render_template("prescribir.html", pid=pid, p=p, v=v, errores=err, alerta=alerta)

if __name__ == "__main__":
    app.run(debug=True)

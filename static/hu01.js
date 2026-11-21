// Vista + controlador de pantalla: únicamente presentación y llamadas HTTP.
// La validación autoritativa se ejecuta en la API y no se duplica aquí.
const mascotaId = document.body.dataset.mascotaId;
const form = document.getElementById("consulta");
const mensaje = document.getElementById("mensaje");
const guardar = document.getElementById("guardar");
const campos = ["fecha", "peso", "sintomas", "diagnostico", "observaciones"];

// Modelo de formulario (MVC): se mantiene en los propios controles del DOM.
const confirmacion = document.getElementById("confirmar_atipicos");
const bloqueConfirmacion = document.getElementById("bloque-confirmacion");

function limpiarMarcas() {
  document.querySelectorAll(".campo").forEach(c => c.classList.remove("invalido", "advertido"));
  document.querySelectorAll(".error").forEach(e => e.textContent = "");
  campos.forEach(c => document.getElementById(c).removeAttribute("aria-invalid"));
}

// clase: "invalido" (error que bloquea) o "advertido" (dato poco habitual que pide confirmación).
function marcar(mensajes, clase) {
  for (const [campo, texto] of Object.entries(mensajes)) {
    const input = document.getElementById(campo);
    const error = document.getElementById("error-" + campo);
    if (input && error) {
      input.closest(".campo").classList.add(clase);
      if (clase === "invalido") input.setAttribute("aria-invalid", "true");
      error.textContent = texto;
    }
  }
  const primer = Object.keys(mensajes)[0];
  if (primer && document.getElementById(primer)) document.getElementById(primer).focus();
}

// La confirmación vale solo para los valores que se mostraron: si cambian, se pide de nuevo.
function reiniciarConfirmacion() {
  confirmacion.checked = false;
  bloqueConfirmacion.hidden = true;
}
["fecha", "peso"].forEach(id => document.getElementById(id).addEventListener("input", reiniciarConfirmacion));

async function cargarContexto() {
  const respuesta = await fetch(`/api/mascotas/${mascotaId}`);
  if (!respuesta.ok) throw new Error("No se pudo cargar el paciente.");
  const p = await respuesta.json();
  document.getElementById("paciente").textContent = `${p.nombre} · ${p.especie} · Peso anterior: ${p.peso_actual} kg`;
  await cargarConsultas();
}

async function cargarConsultas() {
  const respuesta = await fetch(`/api/mascotas/${mascotaId}/consultas`);
  if (!respuesta.ok) throw new Error("No se pudo consultar el historial.");
  const consultas = await respuesta.json();
  const lista = document.getElementById("consultas");
  lista.replaceChildren();
  if (!consultas.length) {
    const item = document.createElement("li"); item.textContent = "Todavía no hay consultas nuevas guardadas.";
    lista.append(item);
  }
  consultas.forEach(c => {
    const item = document.createElement("li");
    item.textContent = `${c.fecha} · ${c.peso} kg · ${c.diagnostico}`;
    lista.append(item);
  });
}

form.addEventListener("submit", async event => {
  event.preventDefault();
  const confirmado = confirmacion.checked;
  guardar.disabled = true;
  mensaje.textContent = "";
  limpiarMarcas();
  const datos = Object.fromEntries(new FormData(form));
  datos.confirmar_atipicos = confirmado;
  try {
    const respuesta = await fetch(`/api/mascotas/${mascotaId}/consultas`, {
      method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(datos)
    });
    const cuerpo = await respuesta.json();
    if (respuesta.status === 422) {
      marcar(cuerpo.errores, "invalido");
      mensaje.className = "mensaje fallo";
      mensaje.textContent = "No se pudo guardar la consulta. Corregí los campos marcados. Los datos cargados se conservaron.";
      return; // No resetear formulario.
    }
    if (respuesta.status === 409) {
      marcar(cuerpo.advertencias, "advertido");
      bloqueConfirmacion.hidden = false;
      confirmacion.checked = false;
      mensaje.className = "mensaje aviso";
      mensaje.textContent = "Hay datos poco habituales (marcados en amarillo). Revisalos: si son correctos, tildá la confirmación y volvé a guardar. Todavía no se guardó nada y los datos cargados se conservaron.";
      return;
    }
    if (!respuesta.ok) throw new Error(cuerpo.error || "No se pudo guardar la consulta.");
    mensaje.className = "mensaje exito";
    mensaje.textContent = cuerpo.mensaje;
    form.reset(); // Solo luego de guardado exitoso.
    reiniciarConfirmacion();
    await cargarContexto();
  } catch (error) {
    mensaje.className = "mensaje fallo";
    mensaje.textContent = error.message;
  } finally {
    guardar.disabled = false;
  }
});

// La fecha inicial es comodidad de uso, no regla de negocio.
document.getElementById("fecha").value = new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().slice(0,10);
cargarContexto().catch(error => { mensaje.className = "mensaje fallo"; mensaje.textContent = error.message; });

// Vista + controlador de pantalla: únicamente presentación y llamadas HTTP.
// La validación autoritativa se ejecuta en la API y no se duplica aquí.
const mascotaId = document.body.dataset.mascotaId;
const form = document.getElementById("consulta");
const mensaje = document.getElementById("mensaje");
const guardar = document.getElementById("guardar");
const campos = ["fecha", "peso", "sintomas", "diagnostico", "observaciones"];

// Modelo de formulario (MVC): se mantiene en los propios controles del DOM.
function mostrarErrores(errores) {
  document.querySelectorAll(".campo").forEach(c => c.classList.remove("invalido"));
  document.querySelectorAll(".error").forEach(e => e.textContent = "");
  campos.forEach(c => document.getElementById(c).removeAttribute("aria-invalid"));
  for (const [campo, texto] of Object.entries(errores)) {
    const input = document.getElementById(campo);
    const error = document.getElementById("error-" + campo);
    if (input && error) {
      input.closest(".campo").classList.add("invalido");
      input.setAttribute("aria-invalid", "true");
      error.textContent = texto;
    }
  }
  const primer = Object.keys(errores)[0];
  if (primer && document.getElementById(primer)) document.getElementById(primer).focus();
}

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
  guardar.disabled = true;
  mensaje.textContent = "";
  mostrarErrores({});
  const datos = Object.fromEntries(new FormData(form));
  try {
    const respuesta = await fetch(`/api/mascotas/${mascotaId}/consultas`, {
      method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(datos)
    });
    const cuerpo = await respuesta.json();
    if (respuesta.status === 422) {
      mostrarErrores(cuerpo.errores);
      mensaje.className = "mensaje fallo";
      mensaje.textContent = "No se pudo guardar la consulta. Corregí los campos marcados. Los datos cargados se conservaron.";
      return; // No resetear formulario.
    }
    if (!respuesta.ok) throw new Error(cuerpo.error || "No se pudo guardar la consulta.");
    mensaje.className = "mensaje exito";
    mensaje.textContent = cuerpo.mensaje;
    form.reset(); // Solo luego de guardado exitoso.
    await cargarConsultas();
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

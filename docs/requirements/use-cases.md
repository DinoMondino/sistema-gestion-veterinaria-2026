# Especificación de Casos de Uso
Los casos de uso se documentan mediante el formato textual estructurado de Cockburn. 
---

## UC-01: Registrar Nuevo Paciente

* Actor Principal: Médico Veterinario / Asistente o recepcionista
* Precondición: El usuario debe haber iniciado sesión en el sistema y disponer de los datos básicos del paciente y su tutor.
* Flujo Principal (Escenario Éxito):
  1. El usuario selecciona la opción de registrar un nuevo paciente en el sistema.
  2. El sistema solicita los datos obligatorios: especie, raza, nombre o número identificador, fecha de nacimiento/edad, peso inicial y datos de identificación del tutor (o datos del establecimiento rural si es animal de producción).
  3. El usuario ingresa los datos solicitados.
  4. El sistema valida que los campos requeridos estén completos y con formato válido.
  5. El sistema registra el paciente en la base de datos y genera un identificador único.
  6. El sistema muestra un mensaje de éxito y despliega la ficha clínica recién creada.
* Flujos Alternativos:
  * 4a. Datos incompletos o erróneos:
    1. El sistema señala los campos faltantes o con formato inválido.
    2. El usuario corrige los datos y reintenta la operación (retorna al paso 4).
* Postcondición: El paciente queda registrado en el sistema con su respectiva ficha clínica e historial base inicializado.

---

## UC-02: Registrar Consulta Clínica

* Actor Principal: Médico Veterinario
* Precondición: El paciente debe estar previamente registrado en el sistema.
* Flujo Principal (Escenario Éxito):
  1. El veterinario busca y selecciona al paciente en el sistema mediante su identificador o nombre.
  2. El sistema muestra el historial clínico general del paciente (último peso, vacunas, patologías previas).
  3. El veterinario selecciona la opción de agregar nueva consulta clínica.
  4. El veterinario ingresa los datos de la consulta: fecha, peso actual, síntomas detectados, diagnóstico preliminar y tratamiento o medicación recetada.
  5. El sistema valida la información ingresada y verifica alertas elementales (por ejemplo, interacciones medicamentosas o tiempos de carencia).
  6. El sistema guarda la consulta y actualiza automáticamente los datos vigentes del paciente (como el peso actual).
  7. El sistema confirma el almacenamiento exitoso del registro clínico.
* Flujos Alternativos:
  * 5a. Alerta por interacción medicamentosa o contraindicación:
    1. El sistema muestra una advertencia detallando la posible interacción o riesgo detectado.
    2. El veterinario evalúa la advertencia y puede decidir modificar la prescripción o justificar el registro bajo su criterio clínico.
    3. El sistema registra la consulta incluyendo la observación de la alerta.
* Postcondición: La consulta clínica queda asociada al historial del paciente de forma trazable y segura.

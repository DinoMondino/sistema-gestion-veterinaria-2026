PRAGMA foreign_keys = ON;

CREATE TABLE veterinario (
    id     INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE mascota (
    id          INTEGER PRIMARY KEY,
    nombre      TEXT NOT NULL,
    especie     TEXT NOT NULL,
    peso_actual TEXT NOT NULL
);

CREATE TABLE historia_clinica (
    id         INTEGER PRIMARY KEY,
    mascota_id INTEGER NOT NULL UNIQUE REFERENCES mascota(id)
);

CREATE TABLE consulta (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    historia_id    INTEGER NOT NULL REFERENCES historia_clinica(id),
    veterinario_id INTEGER NOT NULL REFERENCES veterinario(id),
    fecha          TEXT NOT NULL,
    peso           TEXT NOT NULL,
    sintomas       TEXT NOT NULL,
    diagnostico    TEXT NOT NULL,
    observaciones  TEXT NOT NULL DEFAULT ''
);

INSERT INTO veterinario VALUES (1, 'Dra. Ana Ríos');
INSERT INTO mascota VALUES (1, 'Luna', 'Perro', '6.8'), (2, 'Toby', 'Gato', '4.1');
INSERT INTO historia_clinica VALUES (1, 1), (2, 2);

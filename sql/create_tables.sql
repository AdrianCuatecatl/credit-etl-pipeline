CREATE TABLE IF NOT EXISTS convenios (
    id_convenio TEXT PRIMARY KEY,
    nombre_convenio TEXT,
    tipo TEXT,
    fecha_inicio DATE
);

CREATE TABLE IF NOT EXISTS creditos (
    id_credito TEXT PRIMARY KEY,
    id_cliente TEXT,
    id_convenio TEXT,
    fecha_apertura DATE,
    monto NUMERIC,
    tasa NUMERIC,
    estatus TEXT,
    FOREIGN KEY (id_convenio) REFERENCES convenios(id_convenio)
);

CREATE TABLE IF NOT EXISTS pagos (
    id_pago TEXT PRIMARY KEY,
    id_credito TEXT,
    fecha_pago DATE,
    monto_pago NUMERIC,
    FOREIGN KEY (id_credito) REFERENCES creditos(id_credito)
);
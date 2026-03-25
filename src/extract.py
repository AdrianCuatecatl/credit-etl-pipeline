import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

n_creditos = 500
n_clientes = 150
n_convenios = 50

fecha_inicio = datetime(2023, 1, 1)
fecha_fin = datetime(2025, 12, 31)
dias_rango = (fecha_fin - fecha_inicio).days

data = []

for i in range(1, n_creditos + 1):
    id_credito = f"CRED{i:04d}"
    id_cliente = f"CLI{random.randint(1, n_clientes):04d}"
    id_convenio = f"CONV{random.randint(1, n_convenios):04d}"
    fecha_apertura = fecha_inicio + timedelta(days=random.randint(0, dias_rango))
    monto = random.randint(5000, 250000)

    if monto < 20000:
        tasa = round(random.uniform(28, 45), 2)
    elif monto < 80000:
        tasa = round(random.uniform(20, 32), 2)
    else:
        tasa = round(random.uniform(12, 24), 2)

    if tasa >= 30:
        estatus = random.choices(
            ["Activo", "Liquidado", "Vencido", "Cancelado"],
            weights=[35, 20, 30, 15],
            k=1
        )[0]
    else:
        estatus = random.choices(
            ["Activo", "Liquidado", "Vencido", "Cancelado"],
            weights=[55, 30, 8, 7],
            k=1
        )[0]

    data.append([
        id_credito,
        id_cliente,
        id_convenio,
        fecha_apertura.strftime("%Y-%m-%d"),
        monto,
        tasa,
        estatus
    ])

df = pd.DataFrame(data, columns=[
    "id_credito",
    "id_cliente",
    "id_convenio",
    "fecha_apertura",
    "monto",
    "tasa",
    "estatus"
])

df.to_csv("data/raw/creditos.csv", index=False, encoding="utf-8-sig")
print("Archivo creditos.csv regenerado correctamente.")
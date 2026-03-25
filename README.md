# Credit ETL Pipeline

Pipeline ETL orientado a datos de riesgo crediticio, diseñado para simular un flujo real de ingestión, transformación y carga de información financiera.

## Objetivo

Construir un proceso reproducible que permita:

- Integrar datos de créditos, pagos y convenios
- Modelar relaciones entre entidades financieras
- Ejecutar consultas de negocio sobre cartera
- Validar calidad e integridad de datos

## Tecnologías

- Python (pandas)
- SQL (SQLite para entorno local)
- SQLAlchemy

## Flujo del pipeline

1. Extract
   - Generación de datos simulados de créditos con lógica de negocio

2. Transform
   - Tipificación de datos
   - Validación de nulos
   - Limpieza de datos

3. Load
   - Creación de tablas
   - Inserción de datos en base relacional

4. Análisis
   - Consultas SQL para:
     - Colocación de cartera
     - Distribución por estatus
     - Recuperación de crédito
     - Desempeño por convenio

## Cómo ejecutar

### 1. Instalar dependencias
python -m pip install -r requirements.txt

### 2. Generar datos
python src/extract.py

### 3. Cargar a base
python src/load.py

### 4. Ejecutar análisis
python src/main.py

## Resultados esperados

- Base de datos relacional funcional
- Métricas de negocio sobre cartera crediticia
- Pipeline reproducible end-to-end

## Notas

Este proyecto utiliza SQLite para facilitar su ejecución local, pero está diseñado para escalar a motores como SQL Server o PostgreSQL.
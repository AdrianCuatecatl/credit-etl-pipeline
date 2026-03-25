SELECT 'convenios' AS tabla, COUNT(*) AS total_registros
FROM convenios

UNION ALL

SELECT 'creditos' AS tabla, COUNT(*) AS total_registros
FROM creditos

UNION ALL

SELECT 'pagos' AS tabla, COUNT(*) AS total_registros
FROM pagos;
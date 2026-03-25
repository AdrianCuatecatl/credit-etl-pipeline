-- 1. Total colocado
SELECT 
    COUNT(*) AS total_creditos,
    SUM(monto) AS monto_total
FROM creditos;

-- 2. Distribución por estatus
SELECT 
    estatus,
    COUNT(*) AS total
FROM creditos
GROUP BY estatus;

-- 3. Recuperación de cartera
SELECT 
    c.id_credito,
    c.monto,
    IFNULL(SUM(p.monto_pago), 0) AS total_pagado,
    c.monto - IFNULL(SUM(p.monto_pago), 0) AS saldo_restante
FROM creditos c
LEFT JOIN pagos p ON c.id_credito = p.id_credito
GROUP BY c.id_credito;

-- 4. Desempeño por tipo de convenio
SELECT 
    conv.tipo,
    COUNT(c.id_credito) AS total_creditos,
    SUM(c.monto) AS monto_total
FROM creditos c
JOIN convenios conv ON c.id_convenio = conv.id_convenio
GROUP BY conv.tipo; 
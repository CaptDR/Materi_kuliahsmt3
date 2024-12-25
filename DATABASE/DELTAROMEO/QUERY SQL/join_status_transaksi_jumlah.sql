SELECT 
    ts.status_name AS status_transaksi,
    COUNT(t.transaction_id) AS jumlah_transaksi
FROM 
    transactions t
JOIN 
    transaction_status ts ON t.status_order = ts.status_id
GROUP BY 
    ts.status_name
ORDER BY 
    jumlah_transaksi DESC;

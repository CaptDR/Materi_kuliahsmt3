SELECT 
    u.username AS nama_pengguna,
    SUM(t.total_harga) AS total_pengeluaran
FROM 
    users u
JOIN 
    transactions t ON u.user_id = t.user_id
GROUP BY 
    u.username
ORDER BY 
    total_pengeluaran DESC;

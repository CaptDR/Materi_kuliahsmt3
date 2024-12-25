SELECT 
    u.username AS nama_pengguna,
    t.jumlah_transaksi
FROM 
    users u
JOIN 
    (
        SELECT 
            user_id,
            COUNT(transaction_id) AS jumlah_transaksi
        FROM 
            transactions
        GROUP BY 
            user_id
    ) t ON u.user_id = t.user_id;

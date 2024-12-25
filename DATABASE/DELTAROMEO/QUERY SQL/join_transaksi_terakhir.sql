SELECT 
    u.username AS nama_pengguna,
    t.transaction_id AS id_transaksi_terakhir,
    t.total_harga AS total_harga_transaksi,
    t.created_at AS waktu_transaksi
FROM 
    transactions t
JOIN 
    users u ON t.user_id = u.user_id
WHERE 
    t.created_at = (
        SELECT MAX(t2.created_at)
        FROM transactions t2
        WHERE t2.user_id = t.user_id
    )
ORDER BY 
    t.created_at DESC;

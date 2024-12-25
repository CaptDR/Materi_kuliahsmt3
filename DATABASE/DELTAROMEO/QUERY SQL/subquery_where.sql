SELECT 
    t.transaction_id AS id_transaksi,
    t.total_harga AS total_harga,
    t.created_at AS tanggal_transaksi
FROM 
    transactions t
WHERE 
    t.total_harga > (
        SELECT AVG(total_harga)
        FROM transactions
    );

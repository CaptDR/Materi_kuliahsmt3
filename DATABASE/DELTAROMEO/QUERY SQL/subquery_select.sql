SELECT 
    t.transaction_id AS id_transaksi,
    t.total_harga AS total_harga,
    t.created_at AS tanggal_transaksi,
    (
        SELECT SUM(quantity)
        FROM transactions_items
        WHERE transactions_items.transaction_id = t.transaction_id
    ) AS jumlah_barang
FROM 
    transactions t;
SELECT 
    u.username AS nama_pengguna,
    t.transaction_id AS id_transaksi,
    i.nama_barang AS nama_barang,
    ti.quantity AS jumlah_barang,
    ti.subtotal AS total_harga_per_item
FROM 
    users u
JOIN 
    transactions t ON u.user_id = t.user_id
JOIN 
    transactions_items ti ON t.transaction_id = ti.transaction_id
JOIN 
    barang i ON ti.id_barang = i.id_barang
ORDER BY 
    t.created_at DESC;
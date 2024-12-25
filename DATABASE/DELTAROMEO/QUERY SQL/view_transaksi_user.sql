CREATE VIEW view_user_transactions AS
SELECT 
    u.username AS nama_pengguna,
    t.transaction_id AS id_transaksi,
    t.total_harga AS total_harga_transaksi,
    t.created_at AS waktu_transaksi
FROM 
    users u
JOIN 
    transactions t ON u.user_id = t.user_id;

SELECT 
    i.nama_barang AS nama_barang,
    SUM(ti.quantity) AS total_terjual,
    i.harga AS harga_per_unit
FROM 
    transactions_items ti
JOIN 
    barang i ON ti.id_barang = i.id_barang
GROUP BY 
    i.nama_barang, i.harga
ORDER BY 
    total_terjual DESC
LIMIT 5;

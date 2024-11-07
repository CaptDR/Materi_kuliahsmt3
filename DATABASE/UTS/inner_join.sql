SELECT 
    p.Kode_pengadaan,
    p.Tgl_pengadaan,
    s.Kode_supplier,
    s.Nama_supplier,
    s.Alamat_supplier,
    b.Kode_barang,
    b.Nama_barang,
    bp.Jumlah AS qty,
    b.Harga_satuan,
    bp.Total_harga
FROM 
    Pengadaan p
JOIN 
    Supplier s ON p.Kode_supplier = s.Kode_supplier
JOIN 
    Barang_Pengadaan bp ON p.Kode_pengadaan = bp.Kode_pengadaan
JOIN 
    Barang b ON bp.Kode_barang = b.Kode_barang
WHERE 
    p.Kode_pengadaan = 'PGD002';
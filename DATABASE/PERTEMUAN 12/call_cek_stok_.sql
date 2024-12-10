CALL cek_stok_berdasarkan_kodebrg("BRG_003",
@nama_barang_out, @stok_out);
SELECT @nama_barang_out AS nama_barang,
@stok_out AS stok;
CREATE TABLE Barang_Pengadaan (
    Kode_pengadaan VARCHAR(10),
    Kode_barang VARCHAR(10),
    Jumlah INT,
    Total_harga INT,
    PRIMARY KEY (Kode_pengadaan, Kode_barang),
    FOREIGN KEY (Kode_pengadaan) REFERENCES Pengadaan(Kode_pengadaan),
    FOREIGN KEY (Kode_barang) REFERENCES Barang(Kode_barang)
);
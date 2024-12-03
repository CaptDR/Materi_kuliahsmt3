SELECT MAX(pembelian), MIN(pembelian),
AVG(pembelian)
FROM (SELECT qty AS pembelian FROM
tbl_detailtransaksi) AS tbl_pembelian
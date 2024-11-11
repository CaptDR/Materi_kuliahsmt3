//Membuat Loop dengan FOR
for (let i = 0; i < 10; i++) {
    //template Literal string
    console.log(`ini perulangan ke ${i}`);
    console.log("ini perulangan ke " + i);
    console.log("ini perulangan ke", i);
}

//Membuat Loop dengan FOR
for (let i = 10; i > 0; i--) {
    //template Literal string
    console.log(`ini perulangan ke ${i}`);
    console.log("ini perulangan ke " + i);
    console.log("ini perulangan ke", i);
}

//Loop dengan While
let j = 1;
while (j < 10) {
    console.warn(`ini perulangan While ke ${j}`);
    j++;
}

//Contoh Menampilkan data MHSW
let mhs = ["Budi", "Andi", "Joko"]
for (let i = 0; i < mhs.length; i++) {
    console.log(mhs[i]);
}

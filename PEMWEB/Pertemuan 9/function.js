// Membuat Function
function greetings(name) {
    console.log("Halo, Selamat Datang " + name);
}
greetings("DELTA");

//membuat arrow function
let greetings2 = (name) => {
    console.log("Halo, Sampai Jumpa " + name);
}
greetings2("DELTA");

//Scope Variable Local dan Global
let varGlobal = "Ini Variable Global";
let shapeArea = (panjang, lebar) => {
    let varLocal = "Ini Variable Local";
    console.log(`Luas untuk persegi panjang dengan panjang ${panjang} dan lebar ${lebar} adalah ${panjang * lebar}`);
    console.log(varLocal);
}
shapeArea(5, 10);
// console.log(varLocal);
console.log(varGlobal);
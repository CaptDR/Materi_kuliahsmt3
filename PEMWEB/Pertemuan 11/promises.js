function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const data = "Fetched Data";
            resolve(data);
            reject("Error, Unable to fetch data");
        }, 1000);
    });
}
//Memanggil Promise
fetchData()
    .then((data) => {
        console.log(data);
    })
    .catch((error) => {
        console.error(`Error, Unable to fetch data ${error}`);
    });

//Data Tidak Ada
// function fetchData() {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             const data = "";
//             if (data) {
//                 resolve(data);
//             } else {
//                 reject("Data Tidak Ada");
//             }
function fetchData(callback) {
    setTimeout(function () {
        const data = 'Fetched Data!';
        callback(data);
    }, 5000)
}
fetchData(function (data) {
    console.log(data);
});
console.log("Ini Proses 2");
//Membuat objek untuk menampung XMLHTTPREQUEST
var xhr = new XMLHttpRequest();
//Membuat GET untuk mengambil data
xhr.open("GET", "https://jsonplaceholder.typicode.com/posts?_limit=5", true);
//if untuk menangani perubahan data server
xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
        var responseData = JSON.parse(xhr.responseText);
        // console.log(responseData);
        // Menampilkan data ke elemen HTML
        let container = document.getElementById("container");
        responseData.forEach((item) => {
            const div = document.createElement("div");
            div.innerHTML = `<h3>${item.title}</h3>
            <p>${item.body}</p>`;
            container.appendChild(div);
        });
    }
};
xhr.send();
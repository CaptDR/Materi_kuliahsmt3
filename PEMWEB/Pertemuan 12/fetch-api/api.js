fetch("https://jsonplaceholder.typicode.com/posts").then((response) => {
    if (!response.ok) {
        throw new Error("Network Response Error");
    }
    return response.json();
}).then((data) => {
    console.log(data);
}).catch((error) => {
    console.error("Error : ", error);
});
function Get()
{
    fetch("http://localhost:8000/student/api")
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))
}

function Create() {

    fetch("http://localhost:8000/student/api/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name:"Student21",
            age:28
        })
    })
    .then(response => response.json())
    .then(data => {
        alert("New User Created!");
        console.log(data);
    })
    .catch(error => console.log("Error:", error));
}

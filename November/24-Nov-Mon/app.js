async function FetchMessage()
{
       fetch("http://127.0.0.1:8000/")
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        document.getElementById("msg").innerHTML = data.message;
    })
    .catch(error => console.error('Fetch error:', error));
}


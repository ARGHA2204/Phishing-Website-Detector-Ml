async function checkURL() {
    const url = document.getElementById("url").value;
    const result = document.getElementById("result");

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: url })
        });

        const data = await response.json();

        result.innerText = data.result;

    } catch (error) {
        console.error(error);
        result.innerText = "Error connecting to server";
    }
}
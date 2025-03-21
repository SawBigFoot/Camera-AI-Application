function runAIModel() {
    document.getElementById("loading").style.display = "block";

    fetch("/run-ai-model", { method: "POST" })
        .then(response => response.json())  // Convert response to JSON
        .then(data => {
            document.getElementById("loading").style.display = "none";
            if (data.error) {
                alert("Error: " + data.error);  // Handle error properly
            } else {
                alert(data.message);  // Display the success message
            }
        })
        .catch(error => {
            document.getElementById("loading").style.display = "none";
            alert("Error executing AI Model: " + error);
        });
}

function sendMessage() {
    var messageInput = document.getElementById("message-input");
    var message = messageInput.value;

    if (message.trim() === "") {
        return; // Ignore empty messages
    }

    fetch('/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
    .then(function(response) {
        if (response.ok) {
            console.log("Message sent: " + message);
            // Add the message to the message container
            var messageContainer = document.getElementById("messages"); // Updated ID here
            var messageElement = document.createElement("div");
            messageElement.classList.add("message");
            messageElement.textContent = message;
            messageContainer.appendChild(messageElement);
            // Scroll the message container to the bottom
            messageContainer.scrollTop = messageContainer.scrollHeight;
        } else {
            console.error("Error sending message: " + response.statusText);
        }
    })
    .catch(function(error) {
        console.error("Error sending message: " + error);
    });

    // Clear the input field
    messageInput.value = "";
}
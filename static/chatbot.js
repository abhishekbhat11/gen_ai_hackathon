document.getElementById('send-btn').addEventListener('click', function () {
    let userInput = document.getElementById('user-input').value;
    if (userInput.trim() === "") return;

    let chatBox = document.getElementById('chat-box');
    let userMessage = `<div class='user-message'>${userInput}</div>`;
    chatBox.innerHTML += userMessage;
    document.getElementById('user-input').value = '';

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Use innerHTML to render the HTML from the markdown response
        let botMessage = `<div class='bot-message'>${data.response}</div>`;
        chatBox.innerHTML += botMessage;
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        console.error('Error:', error);
        let errorMessage = `<div class='bot-message error'>Sorry, something went wrong.</div>`;
        chatBox.innerHTML += errorMessage;
    });
});

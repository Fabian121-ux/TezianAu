document.addEventListener("DOMContentLoaded", () => {
    const textarea = document.querySelector(".message-input textarea");
    const sendButton = document.querySelector(".message-input button");
    const chatArea = document.querySelector(".chat-area");

    // Auto-adjust textarea height based on content
    textarea.addEventListener("input", () => {
        textarea.style.height = "auto";
        textarea.style.height = `${textarea.scrollHeight}px`;
    });

    
    // Function to create and display a typing effect
    function displayTypingEffect(text) {
        const message = document.createElement("p");
        message.className = "chatbot-message";
        message.style.color = "#bbb";
        chatArea.appendChild(message);

        let index = 0;
        const typingEffect = setInterval(() => {
            message.textContent += text[index];
            index++;
            if (index === text.length) {
                clearInterval(typingEffect);
                message.scrollIntoView({ behavior: "smooth", block: "end" });
            }
        }, 50); // Adjust typing speed here
    }

    // Send message function
    function sendMessage() {
        const userInput = textarea.value.trim();
        if (userInput) {
            // Display user message
            const userMessage = document.createElement("p");
            userMessage.className = "user-message";
            userMessage.textContent = userInput;
            userMessage.style.color = "#4CAF50";
            chatArea.appendChild(userMessage);

            // Process input for response
            const lowercaseInput = userInput.toLowerCase();
            let response = `I'm sorry, I don't understand. I still have some limitations. Perhaps you can try training me: <a href="training_AI.html">Train me </a>`;

            // Check for matching keyword in lowercase
            for (const keyword in keywords) {
                if (lowercaseInput.includes(keyword)) {
                    response = keywords[keyword];
                    break;
                }
            }

            // Display chatbot's typing effect and response
            const botMessage = document.createElement("p");
            botMessage.className = "chatbot-message";
            botMessage.style.color = "#bbb";
            botMessage.innerHTML = response; // Use innerHTML for links

            chatArea.appendChild(botMessage);
            botMessage.scrollIntoView({ behavior: "smooth", block: "end" });
            textarea.value = ""; // Clear the input
        }
    }

    // Event listener for send button
    sendButton.addEventListener("click", sendMessage);

    // Allow pressing Enter to send a message
    textarea.addEventListener("keydown", (event) => {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault(); // Prevent new line
            sendMessage();
        }
    });
});
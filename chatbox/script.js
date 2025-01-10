// Elements
const usernameInput = document.getElementById('username');
const authButton = document.getElementById('auth-button');
const usernamePage = document.getElementById('username-page');
const uploadPage = document.getElementById('upload-page');
const uploadCircle = document.getElementById('upload-circle');
const profileImgInput = document.getElementById('profile-img-input');
const nextButton = document.getElementById('next-button');
const chatbotPage = document.getElementById('chatbot-page');
const userProfileImg = document.getElementById('user-profile-img');
const userNameDisplay = document.getElementById('user-name');
const darkModeToggle = document.getElementById('dark-mode-toggle');

let username ='';
let profileImgUrl = '';

// Check if elements exist before adding event listeners
if (usernameInput && authButton) {
    // Enable the Auth button when the username is entered
    usernameInput.addEventListener('input', function() {
        username = usernameInput.value.trim();
        authButton.disabled = username === '';
    });

    // Authenticate and move to the profile image upload page
    authButton.addEventListener('click', function() {
        if (usernamePage && uploadPage) {
            usernamePage.style.display = 'none';
            uploadPage.style.display = 'block';
        }
    });
}

if (uploadCircle && profileImgInput) {
    // Open file upload dialog on click of the camera icon
    uploadCircle.addEventListener('click', function() {
        profileImgInput.click();
    });
}

if (nextButton && profileImgInput) {
    // Move to chats.html after uploading profile image
    nextButton.addEventListener('click', function() {
        const file = profileImgInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                profileImgUrl = e.target.result;
                
                // Save data to localStorage
                localStorage.setItem('profileImgUrl', profileImgUrl);
                localStorage.setItem('username', username);
                
                // Navigate to chats.html
                window.location.href = 'chats.html';
            };
            reader.readAsDataURL(file);
        } else {
            alert('Please upload a profile image.');
        }
    });
}

if (darkModeToggle) {
    // Toggle between dark mode and light mode
    darkModeToggle.addEventListener('change', function() {
        if (darkModeToggle.checked) {
            document.body.style.backgroundColor = '#333';
            document.body.style.color = '#fff';
        } else {
            document.body.style.backgroundColor = '#f4f4f4';
            document.body.style.color = '#000';
        }
    });
}

// Retrieve and display profile image and username from localStorage
document.addEventListener('DOMContentLoaded', () => {
    const storedProfileImgUrl = localStorage.getItem('profileImgUrl');
    const storedUsername = localStorage.getItem('username');

    if (storedProfileImgUrl && userProfileImg) {
        userProfileImg.src = storedProfileImgUrl;
    }
    if (storedUsername && userNameDisplay) {
        userNameDisplay.textContent = storedUsername;
    }
});

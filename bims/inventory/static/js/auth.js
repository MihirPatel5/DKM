// auth.js
document.getElementById("loginForm")?.addEventListener("submit", function(event) {
    event.preventDefault();

    const email = this.email.value;
    const password = this.password.value;

    fetch('/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Login failed');
        }
        return response.json();
    })
    .then(data => {
        // Save tokens and redirect
        localStorage.setItem('refreshToken', data.refresh);
        localStorage.setItem('accessToken', data.access);
        window.location.href = '/projects/';
    })
    .catch(error => {
        document.getElementById("loginError").innerText = error.message;
    });
});

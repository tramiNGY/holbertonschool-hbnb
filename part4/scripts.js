/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();
              
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
            
        await loginUser(email, password);
        });
    }
});

async function loginUser(email, password) {
    const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password }),
    });


    if (response.ok) {
        const data = await response.json();
        document.cookie = `token=${data.access_token}; path=/`;
        console.log("Cookie after login", document.cookie); // debug log to verify cookie put winow location in comments
        window.location.href = 'index.html';
    } else {
        alert('Login failed: ' + response.statusText);
    }
  }


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

    checkAuthentication();
    setupPriceFilter();
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
        console.log("Cookie after login", document.cookie); // debug log to verify cookie
    } else {
        alert('Login failed: ' + response.statusText);
    }
}

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!loginLink) {
        console.error('login-link element not found!');
    }

    if (!token) {
        loginLink.style.display = 'block'; // Show the login link
    } else {
        loginLink.style.display = 'none'; // Hide the login link
        fetchPlaces(token); // Call fetchPlaces if the user is logged in
    }
}

function getCookie(name) {
    const cookies = document.cookie.split('; ');
    for (let cookie of cookies) {
        const [cookieName, cookieValue] = cookie.split('=');
        if (cookieName === name) {
            return cookieValue;
        }
    }
    return null;
}

async function fetchPlaces(token) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/places', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Fetched places data:', data);
            displayPlaces(data);
        } else {
            console.error('Failed to fetch places:', response.statusText);
        }
    } catch (error) {
        console.error('Error fetching places:', error);
    }
}

// Function to display the places
function displayPlaces(places) {
    const placesContainer = document.getElementById('places-container');
    placesContainer.innerHTML = '';

    places.forEach(place => {
        const placeElement = document.createElement('div');
        placeElement.classList.add('place');
        placeElement.innerHTML = `
            <h3>${place.title}</h3>
            <p>Description: ${place.description}</p>
            <p>Price: ${place.price}€</p>
            <p>Latitude: ${place.latitude}</p>
            <p>Longitude: ${place.longitude}</p>
            
        `;
        placesContainer.appendChild(placeElement);
    });
}

function setupPriceFilter() {
    const priceFilter = document.getElementById('price-filter');
    priceFilter.addEventListener('change', (event) => {
        const selectedPrice = event.target.value;
        filterPlacesByPrice(selectedPrice);
    });
}

function filterPlacesByPrice(selectedPrice) {
    const places = document.querySelectorAll('.place');
    
    places.forEach(placeElement => {
        const price = parseInt(placeElement.querySelector('p:nth-child(3)').textContent.replace('Price: ', ''), 10);
        
        if (selectedPrice === 'All' || price <= selectedPrice) {
            placeElement.style.display = 'block';
        } else {
            placeElement.style.display = 'none';
        }
    });
}

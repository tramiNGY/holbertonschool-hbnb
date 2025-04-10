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
        window.location.href = 'index.html';
    } else {
        alert('Login failed: ' + response.statusText);
    }
}

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (window.location.pathname.includes('index.html')) {
        if (loginLink) {
            if (!token) {
                loginLink.style.display = 'block';
            } else {
                loginLink.style.display = 'none';
            }
        }
    }
    fetchPlaces(token);
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
            },
            credentials: 'include',
        });

        if (response.ok) {
            const data = await response.json();
            displayPlaces(data);
        } else {
            console.error('Failed to fetch places:', response.statusText);
        }
    } catch (error) {
        console.error('Error fetching places:', error);
    }
}

function displayPlaces(places) {
    const placesContainer = document.getElementById('places-list');
    placesContainer.innerHTML = '';

    if (places && places.length > 0) {
        places.forEach(place => {
            const placeElement = document.createElement('div');
            placeElement.classList.add('place');
            
            placeElement.innerHTML = `
                <h3>${place.title}</h3>
                <p>Description: ${place.description}</p>
                <p class="place-price">Price: ${place.price}€</p>
                <button class="view-details" data-place-id="${place.id}" data-title="${place.title}" data-description="${place.description}" data-price="${place.price}" data-reviews='${JSON.stringify(place.reviews)}' data-amenities='${JSON.stringify(place.amenities)}'>View Details</button>
            `;
            placesContainer.appendChild(placeElement);
        });

        document.querySelectorAll('.view-details').forEach(button => {
            button.addEventListener('click', (event) => {
                const placeDetails = event.target.dataset;
                const queryString = new URLSearchParams(placeDetails).toString();
                window.location.href = `place.html?${queryString}`;
            });
        });
    } else {
        placesContainer.innerHTML = '<p>No places found.</p>';
    }
}

function setupPriceFilter() {
    const priceFilter = document.getElementById('price-filter');
    
    if (priceFilter) {
        priceFilter.addEventListener('change', (event) => {
            const selectedPrice = event.target.value;
            filterPlacesByPrice(selectedPrice);
        });
    }
}

function filterPlacesByPrice(selectedPrice) {
    const places = document.querySelectorAll('.place');
    
    places.forEach(placeElement => {
        const price = parseFloat(placeElement.querySelector('.place-price').textContent.replace('Price: ', '').replace('€', '').trim());
        
        if (selectedPrice === 'All' || price <= selectedPrice) {
            placeElement.style.display = 'block';
        } else {
            placeElement.style.display = 'none';
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const title = urlParams.get('title');
    const description = urlParams.get('description');
    const price = urlParams.get('price');
    const placeId = urlParams.get('place_id');
    const reviews = JSON.parse(decodeURIComponent(urlParams.get('reviews') || '[]'));
    const amenities = JSON.parse(decodeURIComponent(urlParams.get('amenities') || '[]'));

    displayPlaceDetails(title, description, price, reviews, amenities, placeId);
});

function displayPlaceDetails(title, description, price, reviews, amenities, placeId) {
    const placeDetailsContainer = document.getElementById('place-info');
    const reviewsContainer = document.getElementById('reviews');
    const amenitiesContainer = document.getElementById('amenities');

    placeDetailsContainer.innerHTML = `
        <h2>${title}</h2>
        <p><strong>Description:</strong> ${description}</p>
        <p><strong>Price:</strong> ${price}€</p>
        <p><strong>Place ID:</strong> ${placeId}</p>
    `;

    if (reviews && reviews.length > 0) {
        reviewsContainer.innerHTML = `
            <h4>Reviews:</h4>
            ${reviews.map(review => `
                <p><strong>${review.user.first_name} ${review.user.last_name}</strong> - Rating: ${review.rating}</p>
                <p>${review.text}</p>
            `).join('')}
        `;
    } else {
        reviewsContainer.innerHTML = '<p>No reviews available.</p>';
    }

    if (amenities && amenities.length > 0) {
        amenitiesContainer.innerHTML = `
            <h4>Amenities:</h4>
            <ul>
                ${amenities.map(amenity => `<li>${amenity}</li>`).join('')}
            </ul>
        `;
    } else {
        amenitiesContainer.innerHTML = '<p>No amenities listed.</p>';
    }

    const reviewForm = document.getElementById('review-form');
    reviewForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const reviewText = document.getElementById('review-text').value;
        const reviewRating = document.getElementById('review-rating').value;
        const user = { first_name: 'John', last_name: 'Doe' };
        const review = { user, text: reviewText, rating: reviewRating };

        reviews.push(review);
        displayPlaceDetails(title, description, price, reviews, amenities, placeId);
    });
}

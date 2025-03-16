-- Create 'users' table
CREATE TABLE users (
    id CHAR(36) PRIMARY KEY, -- UUID format
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255), -- This will store the hashed password
    is_admin BOOLEAN DEFAULT FALSE
);

-- Create 'places' table
CREATE TABLE places (
    id CHAR(36) PRIMARY KEY, -- UUID format
    title VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2),
    latitude FLOAT,
    longitude FLOAT,
    owner_id CHAR(36), -- Foreign key referencing users(id)
    FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create 'reviews' table
CREATE TABLE reviews (
    id CHAR(36) PRIMARY KEY, -- UUID format
    text TEXT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    user_id CHAR(36), -- Foreign key referencing users(id)
    place_id CHAR(36), -- Foreign key referencing places(id)
    UNIQUE(user_id, place_id), -- Ensure a user can only leave one review per place
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE
);

-- Create 'amenities' table
CREATE TABLE amenities (
    id CHAR(36) PRIMARY KEY, -- UUID format
    name VARCHAR(255) UNIQUE
);

-- Create 'place_amenities' table (Many-to-Many relationship)
CREATE TABLE place_amenities (
    place_id CHAR(36), -- Foreign key referencing places(id)
    amenity_id CHAR(36), -- Foreign key referencing amenities(id)
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenities(id) ON DELETE CASCADE
);


-- Insert initial data into the 'users' table
-- The password must be hashed, here's an example for the hashed password
-- NOTE: Replace 'hashed_admin1234' with the actual hashed password
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES
('36c9050e-ddd3-4c3b-9731-9f487208bbc1', 'Admin', 'HBnB', 'admin@hbnb.io', 'hashed_admin1234', TRUE);

-- Insert initial data into the 'amenities' table
-- Generate the UUIDs using a UUID generator
INSERT INTO amenities (id, name) VALUES
('xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', 'WiFi'),
('xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', 'Swimming Pool'),
('xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', 'Air Conditioning');

-- Insert a sample place (Replace UUIDs with actual values)
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id)
VALUES
('xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', 'Ocean View Villa', 'A beautiful oceanfront property', 150.00, 34.0522, -118.2437, '36c9050e-ddd3-4c3b-9731-9f487208bbc1');

-- Insert a sample review (Replace UUIDs with actual values)
INSERT INTO reviews (id, text, rating, user_id, place_id)
VALUES
('xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', 'Great place! Highly recommend.', 5, 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx');

-- Link amenities to the place (place_id and amenity_id should be replaced with actual values)
INSERT INTO place_amenities (place_id, amenity_id) VALUES
('xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'), -- WiFi
('xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'); -- Swimming Pool


# Introduction
The **HBnB** (Holberton BnB) project is a **simplified version of an Airbnb-like application** designed to help users manage and interact with various services such as listing properties, managing user profiles, leaving reviews, and handling amenities. This project has been broken down into several phases, each focusing on specific areas of development to ensure the application is robust, user-friendly, and scalable.

The following documentation outlines the four main phases of the project, each of which builds upon the previous one. These phases include the creation of technical documentation, implementation of core **business logic and API endpoints**, enhancing the** backend with authentication and database integration**, and finally, **developing a simple web client that interacts with the back-end services**. Through these phases, you will gain experience in structuring, implementing, and testing a **full-stack web application**, including both backend and frontend development.

Now, let's explore each of the four parts of the HBnB project in more detail:

## Part 1: Technical Documentation
### Context and Objective
In this initial phase, you will focus on creating comprehensive technical documentation that will serve as the foundation for the development of the HBnB Evolution application. This documentation will help in understanding the **overall architecture**, the detailed design of the business logic, and the interactions within the system.

### Problem Description
You are tasked with documenting the architecture and design of a simplified version of an AirBnB-like application, named HBnB Evolution. The application will allow users to perform the following primary operations:

User Management: Users can register, update their profiles, and be identified as either regular users or administrators.
Place Management: Users can list properties (places) they own, specifying details such as name, description, price, and location (latitude and longitude). Each place can also have a list of amenities.
Review Management: Users can leave reviews for places they have visited, including a rating and a comment.
Amenity Management: The application will manage amenities that can be associated with places.

## Part 2: Implementation of Business Logic and API Endpoints
In this part of the HBnB Project, you will begin the implementation phase of the application based on the design developed in the previous part. The focus of this phase is to **build the Presentation and Business Logic layers of the application using Python and Flask**. You will implement the core functionality by defining the necessary **classes, methods, and endpoints** that will serve as the foundation for the application’s operation.

In this part, you will create the structure of the project, develop the classes that define the business logic, and implement the API endpoints. The goal is to bring the documented architecture to life by setting up the key functionalities, such as creating and managing users, places, reviews, and amenities, while adhering to best practices in API design.

It’s important to note that, at this stage, you will focus only on implementing the core functionality of the API. JWT authentication and role-based access control will be addressed in the next part. The services layer will be built using Flask and the flask-restx extension to create RESTful APIs.

### Objectives
By the end of this project, you should be able to:

Set Up the Project Structure:

Organize the project into a modular architecture, following best practices for Python and Flask applications.
Create the necessary packages for the Presentation and Business Logic layers.
Implement the Business Logic Layer:

Develop the core classes for the business logic, including User, Place, Review, and Amenity entities.
Implement relationships between entities and define how they interact within the application.
Implement the facade pattern to simplify communication between the Presentation and Business Logic layers.
Build RESTful API Endpoints:

Implement the necessary API endpoints to handle CRUD operations for Users, Places, Reviews, and Amenities.
Use flask-restx to define and document the API, ensuring a clear and consistent structure.
Implement data serialization to return extended attributes for related objects. For example, when retrieving a Place, the API should include details such as the owner’s first_name, last_name, and relevant amenities.
Test and Validate the API:

Ensure that each endpoint works correctly and handles edge cases appropriately.
Use tools like Postman or cURL to test your API endpoints.

## Part 3: Enhanced Backend with Authentication and Database Integration
Welcome to Part 3 of the HBnB Project, where you will extend the backend of the application by introducing **user authentication, authorization, and database integration using SQLAlchemy and SQLite for development**. Later, you’ll configure MySQL for production environments. In this part, you will secure the backend, introduce persistent storage, and prepare the application for a scalable, real-world deployment.

### Objectives of the Project
Authentication and Authorization: Implement JWT-based user authentication using Flask-JWT-Extended and role-based access control with the is_admin attribute for specific endpoints.
Database Integration: Replace in-memory storage with SQLite for development using SQLAlchemy as the ORM and prepare for MySQL or other production grade RDBMS.
CRUD Operations with Database Persistence: Refactor all CRUD operations to interact with a persistent database.
Database Design and Visualization: Design the database schema using mermaid.js and ensure all relationships between entities are correctly mapped.
Data Consistency and Validation: Ensure that data validation and constraints are properly enforced in the models.

## Part 4 - Simple Web Client
In this phase, you’ll be focusing on the **front-end development of your application using HTML5, CSS3, and JavaScript ES6**. Your task is to design and implement an interactive user interface that connects with the back-end services you have developed in previous parts of the project.

### Objectives
Develop a user-friendly interface following provided design specifications.
Implement client-side functionality to interact with the back-end API.
Ensure secure and efficient data handling using JavaScript.
Apply modern web development practices to create a dynamic web application.

## AUTHORS
- [Tra Mi NGUYEN](https://github.com/tramiNGY)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Badge](https://badgen.net/badge/icon/github?icon=github&label)
- [Tom DIBELLONIO](https://github.com/totomus83)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Badge](https://badgen.net/badge/icon/github?icon=github&label)
- [Raphael DOTT](https://github.com/Raphaeldott)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Badge](https://badgen.net/badge/icon/github?icon=github&label)

# **HBNB project**

## Introduction
This document outlines the design and structure of HBnB, a vacation rental platform. The purpose of this document is to provide a clear overview of the system architecture, including its key components, relationships, and functionalities.
HBnB is designed to facilitate short-term property rentals by connecting property owners with potential guests. The system allows users to list properties with a list of amenities, search for accommodations, leave reviews, and manage reservations efficiently.

## Scope

This document covers multiple aspects of HBnB’s system design

High-Level Package Diagram:

Class Diagram: Represents the data model, relationships, and key operations for managing users, places, reviews, and amenities.

Sequence Diagrams for API: Illustrates the flow of requests and responses between system components, detailing key API interactions.

## In depth look at the diagrams

## High-Level Package Diagram

# Business Logic Layer

![printf image image (1)](https://pbs.twimg.com/media/Gj01V98XoAEDxxk?format=jpg&name=medium)

## Class User

| Attributes | Type |
| :---------------: |:---------------:|
|+id |UUID4|
|+first_name |str|
|+last_name |str|
|-email |str|
|-password |str|
|-is_admin |bool|
|+is_owner |bool|

| Methods | Parameter | Return Type | Description |
| :---------------: |:---------------:| :---------------:| :---------------:| 
|-register |first_name, last_name, password, email, id| bool | create a new user |
|-update |obj| bool| update already existing user info |
|-delete |id| bool| delete a user |
|-login |email, password| bool| retrive user data |
|-user_type |id| str | check is user is owner and admin |

## Subclass Owner

The Owner class inherits from the User class, Owner class is also depedent of Review class.

| Attributes | Type |
| :---------------: |:---------------:|
|+place |str|

| Methods | Parameter | Return Type | Description |
| :---------------: |:---------------:| :---------------:| :---------------:|
|reply_review | review_id | str | enable user to reply to a review [

## Subclass Admin

The Admin class inherits from the User class.

| Methods | Parameter | Return Type | Description |
| :---------------: |:---------------:| :---------------:|:---------------:|
|promotion | id_user | bool | promote a user to admin |
|demotion | id_user | bool | demote an admin |

## Class Place

The Place class is tied to the subclass Owner by Composition, which means that Place cannot exist without an Owner, therefore if an owner delete his account, their place will be deleted as well, they can't exist without an owner. 

Place class is also aggregated with the class Amenity, they exist indepedently, amenity exists soly to provide a list to Place.

| Attributes | Type |
| :---------------: |:---------------:|
|+id |UUID4|
|+title |str|
|+description |str|
|+price |float|
|+latitude |float|
|+longitude |float|
|+owner |UUID4|
|+amenities_list |list|

| Methods | Parameter | Return Type | Description |
| :---------------: |:---------------:| :---------------:|:---------------:|
|create | title, description, price, latitude, longitude, owner, amenities_list | bool | create a new place tied to an owner with a list of amenities|
|update | title, description, price, amenities_list | bool | update the infos of an already existing place |
|delete | id | bool | delete a place |

## Class Amenity

Amenity class is also aggregated with the class Place, they exist indepedently, amenity exists soly to provide a list to Place.

| Attributes | Type |
| :---------------: |:---------------:|
|+id |UUID4|
|+name |str|
|+description |str|

| Methods | Parameter | Return Type | Description |
| :---------------: |:---------------:| :---------------:|:---------------:|
|create | name, description | bool | create a new amenity |
|update | name, description | bool | update info of an amenity|
|delete | id | bool | delete an amenity |
|list | id | bool | lists the amenities available|

## Class Review

The Review class is tied to the class Place by Composition, which means that Review cannot exist without a Place, therefore if a Place is deleted, their reviews will be deleted as well, they can't exist without a Place. 

If an Owner deletes his account, it also deletes the reviews in his places since Place is tied to Owner by Composition

Review class is depedent of User, without a user there are no reviews.

| Attributes | Type |
| :---------------: |:---------------:|
|+id |UUID4|
|+place_id |UUID4|
|+user_review |UUID4|
|+rating |int|
|+comment |str|

| Methods | Parameter | Return Type | Description |
| :---------------: |:---------------:| :---------------:|:---------------:|
|create | place_id, user_review, rating, comment | bool | create a new review with a rating |
|update | rating, comment | bool | update the review and rating of an alreadyy existing review|
|delete | id | bool | delete a review |
|list_by_place| place_id | list | lists the reviews and rating of a place|

# API Interaction Flow
![printf image image (1)](https://pbs.twimg.com/media/Gj02erqXsAEcYlQ?format=png&name=small)

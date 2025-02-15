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

## Class Diagram

![printf image image (1)](https://pbs.twimg.com/media/Gj01V98XoAEDxxk?format=jpg&name=medium)

# Class User

| Attributes | Type |
| :---------------: |:---------------:|
|+first_name |str|
|+last_name |str|
|-email |str|
|-password |str|
|-is_admin |bool|
|+is_owner |bool|


## Sequence Diagrams for API

![printf image image (1)](https://pbs.twimg.com/media/Gj02erqXsAEcYlQ?format=png&name=small)

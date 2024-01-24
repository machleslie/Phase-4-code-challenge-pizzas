## Pizza Restaurants - Flask and React Project

This project consists of a Flask backend serving as an API for managing pizza restaurants and pizzas. The frontend is built with React to provide a user-friendly interface for interacting with the API.
Project Structure
Backend (Flask API)

The backend is implemented in Flask, providing the necessary routes to manage restaurants and pizzas.
Models

    Restaurant: Represents a pizza restaurant.
    Pizza: Represents a type of pizza.
    RestaurantPizza: Represents the association between a restaurant and a pizza, including the price.

### Validations

    Added validations to the RestaurantPizza model:
        The price must be between 1 and 30.

### Routes

    GET /restaurants:
        Returns a list of restaurants in JSON format.
        Example:

        json

    [
      {
        "id": 1,
        "name": "Sottocasa NYC",
        "address": "298 Atlantic Ave, Brooklyn, NY 11201"
      },
      {
        "id": 2,
        "name": "PizzArte",
        "address": "69 W 55th St, New York, NY 10019"
      }
    ]

GET /restaurants/:id:

    Returns details of a specific restaurant, including associated pizzas, in JSON format.
    Example (if the restaurant exists):

    json

{
  "id": 1,
  "name": "Sottocasa NYC",
  "address": "298 Atlantic Ave, Brooklyn, NY 11201",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}

Example (if the restaurant does not exist):

json

    {
      "error": "Restaurant not found"
    }

### DELETE /restaurants/:id:

    Deletes a restaurant by ID along with associated RestaurantPizza records.
    Returns an empty response body if successful.
    Example (if the restaurant exists):

    json

{}

Example (if the restaurant does not exist):

json

    {
      "error": "Restaurant not found"
    }

GET /pizzas:

    Returns a list of pizzas in JSON format.
    Example:

    json

    [
      {
        "id": 1,
        "name": "Cheese",
        "ingredients": "Dough, Tomato Sauce, Cheese"
      },
      {
        "id": 2,
        "name": "Pepperoni",
        "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
      }
    ]

### POST /restaurant_pizzas:

    Creates a new RestaurantPizza associated with an existing Pizza and Restaurant.
    Requires an object with the following properties in the request body:

    json

{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}

If successful, sends back a response with data related to the Pizza.
Example (if successful):

json

{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}

Example (if not successful, with validation errors):

json

        {
          "errors": ["validation errors"]
        }

Frontend (React)

The frontend is built with React to provide an interactive and user-friendly interface for managing restaurants and pizzas.
Components

    MenuManagement:
        Displays tables for pizzas, restaurants, and restaurant pizzas.
        Provides a form for adding new restaurant pizzas.

    RestaurantDetails:
        Displays detailed information about a specific restaurant, including associated pizzas.
        Allows the user to navigate back to the list of restaurants.

    AddRestaurantPizza:
        Form component for adding new restaurant pizzas.
        Clears input fields after successful submission.

How to Run the Project
Backend (Flask API)

    Navigate to the backend directory.

    bash

cd backend

## Install dependencies.

bash

pipenv install
pipenv shell

## Run the Flask application.

bash

    python app.py

Frontend (React)

    Navigate to the frontend directory.

    bash

cd frontend

## Install dependencies.

bash

npm install

## Run the React application.

bash

    npm start

    Open your browser and visit http://localhost:3000 to interact with the application.

Note: Ensure that both the Flask backend and React frontend are running simultaneously.
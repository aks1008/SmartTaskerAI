# SmartTaskerAI Product API

## Overview
This Flask-based API provides endpoints for managing users and shopping list items. It uses SQLite for data storage and supports full CRUD operations for both resources.

## Routes

### Users
- `POST /api/users` — Create a new user (fields: name, email, balance)
- `GET /api/users` — Get all users
- `GET /api/users/<id>` — Get a user by ID
- `PUT /api/users/<id>` — Update a user by ID
- `DELETE /api/users/<id>` — Delete a user by ID

### Shopping List
- `POST /api/shoppinglist` — Create a new shopping list item (fields: itemname, price, category)
- `GET /api/shoppinglist` — Get all shopping list items
- `GET /api/shoppinglist/<id>` — Get a shopping list item by ID
- `PUT /api/shoppinglist/<id>` — Update a shopping list item by ID
- `DELETE /api/shoppinglist/<id>` — Delete a shopping list item by ID

## Database Setup
- The database is initialized using `db-creation.py`, which creates and populates both `users` and `shoppinglist` tables with sample data.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Initialize the database: `python db-creation.py`
3. Start the Flask app: `flask run` or `python run.py`

## Notes
- All API endpoints are prefixed with `/api`.
- The project uses blueprints for modular route organization.

---
For more details, see the code in the `app_routes` folder and the models in `models.py`.

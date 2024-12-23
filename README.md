# FastAPI CRUD with SQLAlchemy and PostgreSQL

This project demonstrates how to build a simple **CRUD (Create, Read, Update, Delete)** API using **FastAPI** as the web framework, **SQLAlchemy** as the ORM, and **PostgreSQL** as the database backend.

## Features

- **Create**: Add new records to the database.
- **Read**: Retrieve records from the database by ID or list all records.
- **Update**: Modify existing records in the database.
- **Delete**: Remove records from the database.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python
- PostgreSQL database
- pip (Python package manager)

## Installation

Follow the steps below to get this project up and running.

### 1. Clone the repository

```
git clone https://github.com/aayush-paliwal/FastAPI-REST.git
cd FastAPI-REST
```

### 2. Create a virtual environment 
Create a virtual environment to isolate project dependencies:

```
python3 -m venv venv
```
Activate the virtual environment:
```
venv\Scripts\activate
```

### 3. Install dependencies
Install the required Python packages using pip:
```
pip install -r requirements.txt
```

### 4. Run the FastAPI app
1. Start the FastAPI server with Uvicorn:
    ```
    uvicorn main:app --reload
    ```

2. Or you can also start ther server using
    ```
    fastapi dev main.py
    ```
Your application should now be running at http://localhost:8000.

### 5. Endpoints
Here are the basic CRUD endpoints available in the application:

- GET /all: Get all Todos 
- GET /todo/{_id}: Get a Todo item by ID
- POST /create: Create a new Todo item.
- PUT /update/{_id}: Update a Todo item by ID
- DELETE /delete/{_id}: Delete a Todo item by ID
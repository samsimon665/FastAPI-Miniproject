# FastAPI User Management API

A RESTful User Management API built using FastAPI, PostgreSQL, SQLAlchemy, and Pydantic.  
The project follows a clean layered architecture with proper validation, password hashing, and structured error handling.

---

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- Pydantic
- Passlib (bcrypt)
- Uvicorn

---

## Project Structure

app/
├── main.py
├── core/ # Configuration
├── db/ # Database engine & session
├── models/ # SQLAlchemy models
├── schemas/ # Pydantic schemas
├── crud/ # Business logic
└── routers/ # API endpoints


---

## Setup Instructions

1. Clone the repository:

git clone <your-repo-url>
cd FastAPI-Miniproject


2. Create virtual environment:

python -m venv venv
venv\Scripts\activate


3. Install dependencies:

pip install -r requirements.txt

4. Create `.env` file in root:

DATABASE_URL=postgresql://username:password@localhost:5432/database_name


5. Run the server:

uvicorn app.main:app --reload


Access API docs at:

http://127.0.0.1:8000/docs


---

## API Endpoints

| Method | Endpoint        | Description      |
|--------|---------------|------------------|
| POST   | /users/       | Create user      |
| GET    | /users/       | Get all users    |
| GET    | /users/{id}   | Get single user  |
| PUT    | /users/{id}   | Update user      |
| DELETE | /users/{id}   | Delete user      |

---

## Features

- Secure password hashing (bcrypt)
- Email uniqueness validation
- Proper HTTP status codes (201, 400, 404, 204)
- Clean separation of concerns
- Dependency injection for DB session
- Environment-based configuration
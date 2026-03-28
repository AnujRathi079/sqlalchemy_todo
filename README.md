## FastAPI + SQLAlchemy To-Do API

A simple backend project built using FastAPI and SQLAlchemy ORM to manage a To-Do system with CRUD operations.

## Features
✅ FastAPI REST API
✅ SQLAlchemy ORM
✅ CRUD operations (Create, Read, Update, Delete)
✅ User ↔ Todo relationship (One-to-Many)
✅ Swagger UI for testing


## Tech Stack
Backend: FastAPI
Database: SQLite
ORM: SQLAlchemy
Validation: Pydantic
Server: Uvicorn

## Project Structure
sqlalchemy_todo/
│
├── main.py          # FastAPI app (routes)
├── models.py        # Database models
├── schemas.py       # Pydantic schemas
├── crud.py          # Database logic
├── database.py      # DB connection
│
├── requirements.txt
└── README.md

## Create Virtual Environment

python -m venv .venv

## Windows
.venv\Scripts\activate\

## Install Dependencies
pip install -r requirements.txt

## Run Server
uvicorn main:app --reload

## API Documentation
http://127.0.0.1:8000/docs
Swagger UI available for testing API

## Concepts Used
ORM (Object Relational Mapping)
FastAPI dependency injection
Database relationships (One-to-Many)
Clean code structure

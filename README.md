# 🚀 Task Management Backend API

This project is a backend service developed using FastAPI, implementing secure user authentication with JWT. It provides core functionalities for managing tasks efficiently through well-structured REST APIs.

---

## 🔹 Key Features

* User signup and login functionality
* Secure authentication using JWT tokens
* Full CRUD operations for task management
* Access control with protected API routes

---

## 🛠️ Technology Stack

* FastAPI (Backend Framework)
* SQLAlchemy (ORM)
* SQLite (Database)
* JWT (Authentication Mechanism)

---

## 📌 API Endpoints Overview

### 🔐 Authentication

* `POST /register` → Create a new user account
* `POST /login` → Authenticate user and generate token

---

### 📋 Task Management

* `GET /tasks` → Retrieve all tasks
* `POST /tasks` → Create a new task
* `PUT /tasks/{id}` → Update an existing task
* `DELETE /tasks/{id}` → Remove a task

---

## ▶️ Running the Application

Install dependencies:

pip install -r requirements.txt

Start the server:

uvicorn main:app --reload

---




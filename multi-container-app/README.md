# 🚀 Multi-Container Flask + PostgreSQL App (Docker Compose)

## 📌 Overview

This project demonstrates how to build and run a **multi-container application** using Docker Compose.
It includes:

* Flask web application
* PostgreSQL database
* pgAdmin UI

---

## 🧰 Tech Stack

* Python (Flask)
* PostgreSQL
* Docker
* Docker Compose

---

## 📁 Project Structure

```
multi-container-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
├── .dockerignore
└── README.md
```

---

## ⚙️ Setup & Run

### 1. Clone Repo

```bash
git clone https://github.com/Ashish420-tech/Docker-master.git
cd Docker-master/multi-container-app
```

---

### 2. Create `.env`

```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=mydb
```

---

### 3. Run Containers

```bash
docker-compose up --build
```

Or run in background:

```bash
docker-compose up -d
```

---

## 🌐 Access Application

| Service   | URL                   |
| --------- | --------------------- |
| Flask App | http://localhost:5000 |
| pgAdmin   | http://localhost:5050 |

---

## 🔐 pgAdmin Login

```
Email: admin@example.com
Password: admin
```

### Add Database Server

| Field    | Value    |
| -------- | -------- |
| Host     | db       |
| Port     | 5432     |
| Username | user     |
| Password | password |

---

## 🧠 How It Works

```
Browser → Flask (web container) → PostgreSQL (db container)
                                   ↓
                               pgAdmin (UI)
```

* Docker Compose creates an internal network
* Services communicate using service names (`db`)
* Data is persisted using Docker volumes

---

## 🔍 Troubleshooting

### Port already in use

```bash
docker stop $(docker ps -aq)
```

### Rebuild without cache

```bash
docker-compose build --no-cache
```

---

## 🧠 Key Learnings

* Multi-container architecture
* Docker Compose networking
* Service-to-service communication
* Environment variable management
* Persistent storage using volumes

---

## 🚀 Future Improvements

* Add Gunicorn (production server)
* Add Nginx reverse proxy
* Implement CRUD APIs
* Deploy using Kubernetes

---

## 👨‍💻 Author

Ashish Mondal

---

## ⭐ Contribution

Feel free to fork and improve this project!

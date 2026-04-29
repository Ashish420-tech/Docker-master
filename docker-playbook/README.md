# 🚀 Docker Flask Application

## 📌 Project Overview

This project demonstrates how to containerize a simple Python Flask web application using Docker. It covers the complete workflow from application setup to building and running a Docker container.

---

## 🧰 Tech Stack

* **Language:** Python
* **Framework:** Flask
* **Containerization:** Docker

---

## 📁 Project Structure

```
docker-playbook/
│
├── app.py
├── requirements.txt
└── Dockerfile
```

---

## 🧩 Application Code

### `app.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

### `requirements.txt`

```
flask
```

---

## 🐳 Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

## ⚙️ Build Docker Image

```bash
docker build -t flask-app .
```

---

## ▶️ Run Container

```bash
docker run -p 5000:5000 flask-app
```

---

## 🌐 Access Application

Open your browser and visit:

```
http://localhost:5000
```

Expected output:

```
Hello, Docker!
```

---

## 🔍 Troubleshooting

### ❌ Container exits immediately

* Ensure Flask app is running with `host="0.0.0.0"`

### ❌ Code changes not reflecting

* Rebuild image:

```bash
docker build -t flask-app . --no-cache
```

### ❌ Port not accessible

* Check running containers:

```bash
docker ps
```

---

## 🧠 Key Learnings

* Dockerfile creation and syntax
* Building Docker images
* Running and managing containers
* Understanding Docker layers and caching

---

## 🚀 Future Improvements

* Add Docker Compose
* Use Gunicorn for production
* Deploy on Kubernetes
* Integrate CI/CD pipeline

---

## 👨‍💻 Author

Ashish Mondal

---

## ⭐ Contribute

Feel free to fork this repository and enhance the project.

---

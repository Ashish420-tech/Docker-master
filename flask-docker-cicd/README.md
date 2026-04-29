# 🚀 Flask Docker CI/CD Pipeline

## 📌 Overview

This project demonstrates how to automate Docker image builds and deployments using **CI/CD with GitHub Actions**.

On every push, the pipeline:

* Builds a Docker image
* Pushes it to Docker Hub

---

## 🧰 Tech Stack

* Python (Flask)
* Docker
* GitHub Actions
* Docker Hub

---

## 📁 Project Structure

```
Docker-master/
│
├── flask-docker-cicd/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .dockerignore
│   └── .gitignore
│
├── .github/
│   └── workflows/
│       └── docker.yml
```

---

## ⚙️ How CI/CD Works

```
Code Push → GitHub Actions → Build Docker Image → Push to Docker Hub
```

---

## 🔄 GitHub Actions Workflow

* Trigger: Push to `main` or `flask-docker-cicd`
* Steps:

  1. Checkout code
  2. Login to Docker Hub
  3. Build Docker image
  4. Push image to Docker Hub

---

## 🔑 Required Secrets

Add in GitHub → Settings → Secrets:

| Name            | Description             |
| --------------- | ----------------------- |
| DOCKER_USERNAME | Docker Hub username     |
| DOCKER_PASSWORD | Docker Hub access token |

---

## 🐳 Docker Image

Image is pushed to:

```
docker.io/<your-username>/flask-cicd:latest
```

---

## ▶️ Run Locally

```bash
docker pull <your-username>/flask-cicd:latest
docker run -p 5000:5000 <your-username>/flask-cicd:latest
```

Open:

```
http://localhost:5000
```

---

## 🧠 Key Learnings

* CI/CD pipeline creation
* Docker image automation
* Secure secrets handling
* GitHub Actions workflow design

---

## 🚀 Future Improvements

* Add version tagging (SHA-based images)
* Deploy to AWS EC2 automatically
* Kubernetes deployment
* Add test stage before build

---

## 🎯 Interview Summary

> “I built a CI/CD pipeline using GitHub Actions that automatically builds and pushes Docker images to Docker Hub on every code push.”

---

## 👨‍💻 Author

Ashish Mondal

---

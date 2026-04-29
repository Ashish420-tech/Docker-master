# 🚀 Docker Swarm Load Balancing Project

## 📌 Overview

This project demonstrates how to deploy a **scalable, load-balanced web application** using **Docker Swarm** and **Nginx**.

A Flask-based web app is deployed with multiple replicas, and Nginx acts as a reverse proxy to distribute traffic across containers.

---

## 🏗 Architecture

```
Client → Nginx (Port 80)
            ↓
     Docker Swarm DNS (web)
            ↓
   Multiple Flask Containers (Replicas)
```

---

## 🛠 Tech Stack

* Docker Swarm (Container Orchestration)
* Nginx (Reverse Proxy / Load Balancer)
* Flask (Python Web Application)

---

## 📁 Project Structure

```
docker-swarm-loadbalancer/
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml
├── nginx.conf
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Initialize Docker Swarm

```bash
docker swarm init --advertise-addr <your-ip>
```

---

### 2️⃣ Build & Push Docker Image

```bash
cd app
docker build -t ashishmondal420/swarm-app:latest .
docker push ashishmondal420/swarm-app:latest
```

---

### 3️⃣ Create Docker Config (Required for Nginx)

```bash
docker config create nginx_conf nginx.conf
```

---

### 4️⃣ Deploy Stack

```bash
docker stack deploy -c docker-compose.yml myapp
```

---

## 🔍 Verification

Check running services:

```bash
docker service ls
```

Check replicas:

```bash
docker service ps myapp_web
```

---

## 🌐 Access Application

Open in browser:

```
http://localhost
```

👉 Refresh multiple times to observe **load balancing across containers**

---

## 📈 Scaling Application

Increase replicas dynamically:

```bash
docker service scale myapp_web=5
```

---

## 🧹 Cleanup

```bash
docker stack rm myapp
docker swarm leave --force
```

---

## ⚠️ Common Issues & Fixes

### ❌ Default Nginx Page Showing

✔ Fix:

* Ensure `nginx.conf` is loaded via Docker configs
* Recreate config:

```bash
docker stack rm myapp
docker config rm nginx_conf
docker config create nginx_conf nginx.conf
docker stack deploy -c docker-compose.yml myapp
```

---

### ❌ Network Not Found Error

✔ Fix:

```bash
docker stack rm myapp
sleep 5
docker stack deploy -c docker-compose.yml myapp
```

---

### ❌ Config Already Exists

✔ Fix:

```bash
docker config rm nginx_conf
docker config create nginx_conf nginx.conf
```

---

## 🧠 Key Concepts Learned

* Docker Swarm orchestration
* Overlay networking
* Service replication & scaling
* Nginx reverse proxy configuration
* Docker Configs for production setups

---

## 💼 Resume Highlight

> Implemented a scalable containerized application using Docker Swarm with Nginx-based load balancing and replicated Flask services.

---

## 🚀 Future Enhancements

* Add health checks & auto-healing
* Implement rolling updates (zero downtime)
* CI/CD pipeline with GitHub Actions
* Deploy multi-node Swarm cluster on AWS

---

## 👨‍💻 Author

**Ashish Mondal**
Docker Hub: https://hub.docker.com/u/ashishmondal420

---

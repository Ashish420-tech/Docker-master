# 🚀 Scalable Microservices Architecture with Docker & Kubernetes

## 📌 Overview

This project demonstrates a **production-style microservices architecture** deployed using **Docker and Kubernetes**, with an **NGINX Ingress API Gateway** for routing and scalability.

It consists of three independent services:

* 👤 User Service (Authentication & user data)
* 📦 Product Service (Product catalog)
* 🛒 Order Service (Order processing)

Each service is containerized and deployed using Kubernetes with **scalable replicas and internal service discovery**.

---

## 🧰 Tech Stack

* Docker (Containerization)
* Kubernetes (Orchestration)
* NGINX Ingress Controller (API Gateway)
* Flask (Backend services)
* Minikube (Local Kubernetes cluster)

---

## 🏗️ Architecture

Client → Ingress (API Gateway) → Kubernetes Services → Pods → Microservices

---

## 📂 Project Structure

```
microservices-project/
│
├── user-service/
├── product-service/
├── order-service/
│
├── k8s/
│   ├── user-deployment.yaml
│   ├── product-deployment.yaml
│   ├── order-deployment.yaml
│   └── api-gateway.yaml
│
├── README.md
└── playbook.md
```

---

## ⚙️ Features

* ✅ Microservices-based architecture
* ✅ Dockerized applications
* ✅ Kubernetes deployments with replicas
* ✅ API Gateway using Ingress
* ✅ Host-based routing (`myapp.local`)
* ✅ Scalable and modular design

---

## 🚀 How It Works

* Each service runs inside its own container
* Kubernetes manages deployment and scaling
* Services communicate internally via ClusterIP
* Ingress routes external traffic to services

---

## 🌐 API Endpoints

| Endpoint    | Description        |
| ----------- | ------------------ |
| `/users`    | Fetch user list    |
| `/products` | Fetch product list |
| `/orders`   | Fetch order list   |

---

## 🧪 Sample Output

```json
/users
{"users":["Alice","Bob","Charlie"]}

/products
{"products":[{"id":1,"name":"Laptop"},{"id":2,"name":"Phone"}]}

/orders
{"orders":[{"id":101,"product":"Laptop"},{"id":102,"product":"Phone"}]}
```

---

## 📊 Scaling

Each service uses Kubernetes Deployment with replicas:

```yaml
replicas: 2 or 3
```

---

## 🧠 Key Learnings

* Container orchestration with Kubernetes
* Service discovery and networking
* API Gateway routing using Ingress
* Real-world microservices design principles

---

## 🔥 Future Enhancements

* Add MongoDB/PostgreSQL database
* Implement service-to-service communication
* Add CI/CD pipeline (GitHub Actions)
* Add monitoring (Prometheus + Grafana)
* Deploy on cloud (AWS EKS / GKE)

---

## 👨‍💻 Author

Ashish Mondal
DevOps Engineer | Docker | Kubernetes | Cloud | CI/CD

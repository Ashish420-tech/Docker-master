# 🚀 Kubernetes with Docker – Web App Deployment

## 📌 Project Overview

This project demonstrates how to deploy a containerized Flask application using Kubernetes on a local cluster powered by Minikube.

It covers core DevOps concepts like containerization, orchestration, scaling, and self-healing.

---

## 🧰 Tech Stack

* Docker
* Kubernetes
* Minikube
* Flask (Python)

---

## 🏗️ Architecture

User → Service → Deployment → Pods

(Optional advanced setup)
User → Ingress → Service → Deployment → Pods

---

## ⚙️ Features

* Containerized Flask application
* Kubernetes Deployment with multiple replicas
* LoadBalancer Service for external access
* Horizontal scaling
* Self-healing (auto pod recreation)
* Ingress-based routing (optional)

---

## 📁 Project Structure

docker-kubernetes-project/
├── app.py
├── Dockerfile
├── requirements.txt
├── deployment.yaml
├── service.yaml
├── ingress.yaml (optional)
├── README.md
└── playbook.md

---

## 🚀 Setup Instructions

### 1️⃣ Start Minikube

minikube start --memory=4096 --cpus=2

---

### 2️⃣ Build and Push Docker Image

docker build -t ashishmondal420/k8s-app .
docker push ashishmondal420/k8s-app

---

### 3️⃣ Deploy to Kubernetes

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

---

### 4️⃣ Verify Deployment

kubectl get pods
kubectl get services

---

### 5️⃣ Access Application

minikube service web-service

---

## 📈 Scaling the Application

kubectl scale deployment web-app --replicas=5

---

## 🔁 Self-Healing Demo

kubectl delete pod <pod-name>

Kubernetes will automatically recreate the pod.

---

## 🌐 Ingress Setup (Optional)

Enable ingress:
minikube addons enable ingress

Apply:
kubectl apply -f ingress.yaml

Update hosts file: <minikube-ip> myapp.local

Access:
http://myapp.local

---

## ⚠️ Common Issues & Fixes

### ❌ ErrImagePull / ImagePullBackOff

* Ensure Docker image is pushed to Docker Hub
* Verify correct image name and tag

### ❌ InvalidImageName

* Remove spaces or incorrect syntax in image field

### ❌ API Server Not Running

* Restart Minikube with sufficient resources

---

## 🧠 Learning Outcomes

* Understanding Kubernetes architecture
* Managing deployments and services
* Scaling applications
* Debugging container issues
* Working with Minikube local clusters

---

## 📸 Screenshots (Add Here)

* Running Pods
* Scaling Demo
* Application Output

---

## 📌 Author

Ashish Mondal

# 🛠️ Kubernetes Deployment Playbook

## 🎯 Objective

Deploy a Dockerized Flask application using Kubernetes and demonstrate scaling and self-healing.

---

## 🔧 Tools Used

* Docker
* Kubernetes (kubectl)
* Minikube
* Flask

---

## 🪜 Step-by-Step Execution

### Step 1: Environment Setup

minikube start --memory=4096 --cpus=2

kubectl get nodes

---

### Step 2: Application Containerization

docker build -t ashishmondal420/k8s-app .
docker push ashishmondal420/k8s-app

---

### Step 3: Kubernetes Deployment

kubectl apply -f deployment.yaml

---

### Step 4: Service Exposure

kubectl apply -f service.yaml

---

### Step 5: Verification

kubectl get pods
kubectl get svc

---

### Step 6: Access Application

minikube service web-service

---

## 📈 Scaling Test

kubectl scale deployment web-app --replicas=5

kubectl get pods

---

## 🔁 Self-Healing Test

kubectl delete pod <pod-name>

kubectl get pods -w

---

## 🌐 Ingress Setup (Optional)

minikube addons enable ingress

kubectl apply -f ingress.yaml

---

## 🚨 Issues Faced & Resolutions

### 1. Minikube API Server Stopped

**Issue:**
kubectl not responding, connection reset errors

**Fix:**
minikube delete
minikube start --memory=4096 --cpus=2

---

### 2. ErrImagePull

**Issue:**
Kubernetes could not pull image

**Cause:**
Incorrect Docker Hub username

**Fix:**
docker build -t ashishmondal420/k8s-app .
docker push ashishmondal420/k8s-app

---

### 3. InvalidImageName

**Issue:**
Image name parsing failed

**Cause:**
Used "docker push ..." inside YAML

**Fix:**
Use only:
image: ashishmondal420/k8s-app:latest

---

### 4. ContainerCreating Delay

**Issue:**
Pods stuck in ContainerCreating

**Fix:**
Wait for image pull or check logs

---

## 📊 Key Commands Reference

kubectl get pods
kubectl get svc
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl scale deployment web-app --replicas=5

---

## 🧠 Key Learnings

* Kubernetes manages containers automatically
* Deployment ensures desired state
* Services expose applications
* Pods are ephemeral and self-healing
* Proper image naming is critical

---

## ✅ Final Outcome

* Application successfully deployed on Kubernetes
* Accessible via Minikube service
* Scaling and self-healing verified

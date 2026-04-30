📦 COMPLETE PROJECT STRUCTURE (FINAL)
microservices-project/
│
├── user-service/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .dockerignore
│
├── product-service/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .dockerignore
│
├── order-service/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .dockerignore
│
├── k8s/
│   ├── user-deployment.yaml
│   ├── product-deployment.yaml
│   ├── order-deployment.yaml
│   └── api-gateway.yaml
│
├── README.md
└── playbook.md
🧑‍💻 FULL CODE (ALL FILES)
🔹 user-service
📄 app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
📄 requirements.txt
Flask
📄 Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
📄 .dockerignore
__pycache__/
*.pyc
.git
🔹 product-service
📄 app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify({
        "products": [
            {"id": 1, "name": "Laptop"},
            {"id": 2, "name": "Phone"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
📄 requirements.txt
Flask
📄 Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
📄 .dockerignore
__pycache__/
*.pyc
.git
🔹 order-service
📄 app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify({
        "orders": [
            {"id": 101, "product": "Laptop"},
            {"id": 102, "product": "Phone"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
📄 requirements.txt
Flask
📄 Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
📄 .dockerignore
__pycache__/
*.pyc
.git
☸️ KUBERNETES FILES
📄 k8s/user-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: user-service
  template:
    metadata:
      labels:
        app: user-service
    spec:
      containers:
      - name: user-service
        image: ashishmondal420/user-service:latest
        ports:
        - containerPort: 5001
---
apiVersion: v1
kind: Service
metadata:
  name: user-service
spec:
  selector:
    app: user-service
  ports:
    - port: 80
      targetPort: 5001
  type: ClusterIP
📄 k8s/product-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: product-service
spec:
  replicas: 2
  selector:
    matchLabels:
      app: product-service
  template:
    metadata:
      labels:
        app: product-service
    spec:
      containers:
      - name: product-service
        image: ashishmondal420/product-service:latest
        ports:
        - containerPort: 5002
---
apiVersion: v1
kind: Service
metadata:
  name: product-service
spec:
  selector:
    app: product-service
  ports:
    - port: 80
      targetPort: 5002
  type: ClusterIP
📄 k8s/order-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-service
spec:
  replicas: 2
  selector:
    matchLabels:
      app: order-service
  template:
    metadata:
      labels:
        app: order-service
    spec:
      containers:
      - name: order-service
        image: ashishmondal420/order-service:latest
        ports:
        - containerPort: 5003
---
apiVersion: v1
kind: Service
metadata:
  name: order-service
spec:
  selector:
    app: order-service
  ports:
    - port: 80
      targetPort: 5003
  type: ClusterIP
📄 k8s/api-gateway.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: api-gateway
  annotations:
    kubernetes.io/ingress.class: nginx
spec:
  rules:
  - host: myapp.local
    http:
      paths:
      - path: /users
        pathType: Prefix
        backend:
          service:
            name: user-service
            port:
              number: 80
      - path: /products
        pathType: Prefix
        backend:
          service:
            name: product-service
            port:
              number: 80
      - path: /orders
        pathType: Prefix
        backend:
          service:
            name: order-service
            port:
              number: 80

===================================================

# 🚀 Microservices Project Playbook

## 1. Start Minikube
minikube start

## 2. Enable Ingress
minikube addons enable ingress

## 3. Get IP
minikube ip

## 4. Update Hosts
sudo nano /etc/hosts
# Add:
<minikube-ip> myapp.local

## 5. Build Images
docker build -t <dockerhub>/user-service ./user-service
docker build -t <dockerhub>/product-service ./product-service
docker build -t <dockerhub>/order-service ./order-service

## 6. Push Images
docker push <dockerhub>/user-service
docker push <dockerhub>/product-service
docker push <dockerhub>/order-service

## 7. Deploy
kubectl apply -f k8s/

## 8. Verify
kubectl get pods
kubectl get ingress

## 9. Test
curl http://myapp.local/users
curl http://myapp.local/products
curl http://myapp.local/orders

CI/CD for Dockerized Applications (Jenkins + Kubernetes)
🚀 Project Overview

This project demonstrates an end-to-end CI/CD pipeline for a containerized application using:

Jenkins (Pipeline automation)
Docker (Containerization)
Kubernetes (Deployment)
Minikube (Local cluster)
Flask (Sample web app)
🏗️ Architecture Diagram
🔁 Workflow
Developer → GitHub Repo
        → Jenkins Pipeline
            → Build Docker Image
            → Push to Docker Hub
            → Deploy to Kubernetes
        → Kubernetes Cluster (Minikube)
        → Running Application
📁 Project Structure
Docker-master/
└── ci-cd-docker-app/
    ├── app.py
    ├── Dockerfile
    ├── requirements.txt
    ├── Jenkinsfile
    ├── .dockerignore
    └── k8s/
        └── deployment.yaml
🧱 Application
Flask App (app.py)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Automated CI/CD with Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
🐳 Docker Setup
Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
⚙️ Jenkins Pipeline
pipeline {
    agent any

    environment {
        IMAGE_NAME = "myapp"
        DOCKER_USER = "ashishmondal420"
    }

    stages {

        stage('Build') {
            steps {
                sh '''
                docker build -t $DOCKER_USER/$IMAGE_NAME:latest ./ci-cd-docker-app
                '''
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                    echo $PASS | docker login -u $USER --password-stdin
                    docker push $DOCKER_USER/$IMAGE_NAME:latest
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f ./ci-cd-docker-app/k8s/deployment.yaml
                kubectl rollout restart deployment myapp
                '''
            }
        }
    }
}
☸️ Kubernetes Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp

spec:
  replicas: 2

  selector:
    matchLabels:
      app: myapp

  template:
    metadata:
      labels:
        app: myapp

    spec:
      containers:
      - name: myapp
        image: ashishmondal420/myapp:latest
        imagePullPolicy: Always
        ports:
        - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: myapp

spec:
  selector:
    app: myapp

  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000

  type: LoadBalancer
🌐 Access Application
minikube service myapp

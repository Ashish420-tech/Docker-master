# 📘 Docker Swarm Load Balancer – Playbook / Runbook

---

## 🎯 Objective

Deploy and manage a **scalable, load-balanced web application** using Docker Swarm with Nginx as a reverse proxy.

---

## 🏗 Architecture

```
Client → Nginx (Port 80)
            ↓
     Docker Swarm (Service: web)
            ↓
   Flask App Containers (Replicas)
```

---

## 🛠 Prerequisites

* Docker installed (`docker --version`)
* Docker Hub account (for image push)
* Ports 80 & 2377 available
* System with internet access

---

## ⚙️ Setup Steps

### 🔹 Step 1: Initialize Swarm

```bash
docker swarm init --advertise-addr <your-ip>
```

Verify:

```bash
docker node ls
```

---

### 🔹 Step 2: Build & Push Application Image

```bash
cd app
docker build -t ashishmondal420/swarm-app:latest .
docker push ashishmondal420/swarm-app:latest
```

---

### 🔹 Step 3: Create Docker Config for Nginx

```bash
docker config create nginx_conf nginx.conf
```

---

### 🔹 Step 4: Deploy Stack

```bash
docker stack deploy -c docker-compose.yml myapp
```

---

## 🔍 Validation & Health Checks

### ✅ Check Services

```bash
docker service ls
```

### ✅ Check Replicas

```bash
docker service ps myapp_web
```

### ✅ Check Logs

```bash
docker service logs myapp_nginx
docker service logs myapp_web
```

---

## 🌐 Functional Testing

### Browser Test

```
http://localhost
```

### CLI Test

```bash
for i in {1..5}; do curl localhost; done
```

Expected:

* Different container hostnames (load balancing)

---

## 📈 Scaling Operations

Increase replicas:

```bash
docker service scale myapp_web=5
```

Verify:

```bash
docker service ls
```

---

## 🔁 Deployment Updates

### Update Image Version

```bash
docker service update --image ashishmondal420/swarm-app:latest myapp_web
```

---

## 🚨 Incident Handling / Troubleshooting

---

### ❌ Issue: Default Nginx Page Showing

**Cause:**

* Nginx config not loaded properly

**Fix:**

```bash
docker stack rm myapp
docker config rm nginx_conf
docker config create nginx_conf nginx.conf
docker stack deploy -c docker-compose.yml myapp
```

---

### ❌ Issue: Nginx Container Failing

Check logs:

```bash
docker service logs myapp_nginx
```

Fix:

* Validate `nginx.conf`
* Ensure correct syntax

---

### ❌ Issue: Network Not Found

**Cause:**

* Stack removed and redeployed too quickly

**Fix:**

```bash
docker stack rm myapp
sleep 5
docker stack deploy -c docker-compose.yml myapp
```

---

### ❌ Issue: Config Already Exists

**Fix:**

```bash
docker config rm nginx_conf
docker config create nginx_conf nginx.conf
```

---

### ❌ Issue: Config In Use

**Fix:**

```bash
docker stack rm myapp
docker config rm nginx_conf
```

---

## 🔐 Security Best Practices

* Use Docker Secrets for sensitive data
* Avoid exposing unnecessary ports
* Use minimal base images
* Scan images for vulnerabilities

---

## 📊 Monitoring (Optional Enhancements)

* Use Prometheus + Grafana
* Docker Swarm metrics exporters
* Container logs via ELK stack

---

## 🧹 Cleanup

```bash
docker stack rm myapp
docker swarm leave --force
```

---

## 📌 Key Learnings

* Swarm orchestration basics
* Overlay networking
* Load balancing with Nginx
* Docker Configs vs Volumes
* Service scaling & updates

---

## 💼 Production Notes

* Prefer multi-node Swarm cluster
* Use load balancer (ALB/NLB) in front
* Enable rolling updates & health checks
* Automate deployment via CI/CD

---

## 👨‍💻 Author

Ashish Mondal
Docker Hub: https://hub.docker.com/u/ashishmondal420

---

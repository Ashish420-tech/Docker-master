🔐 Secure Docker Deployment with Traefik & Let’s Encrypt
🚀 Overview

This project demonstrates a production-ready deployment of a containerized web application using:

🐳 Docker & Docker Compose
🌐 Traefik (Reverse Proxy & Load Balancer)
🔒 Let’s Encrypt (Automatic SSL Certificates)
🔐 Basic Authentication
🐍 Flask Web Application
🧭 Architecture
7
🔁 Request Flow
User → Domain (DNS) → Server IP → Traefik → Flask App
                         ↓
                   SSL Termination
                         ↓
                  Basic Authentication
⚙️ Tech Stack
Tool	Purpose
Docker	Containerization
Docker Compose	Multi-container orchestration
Traefik	Reverse proxy & routing
Let’s Encrypt	Free SSL certificates
Flask	Backend application
📁 Project Structure
secure-traefik-docker/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── traefik.yml
└── letsencrypt/
    └── acme.json
🛠️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/secure-traefik-docker.git
cd secure-traefik-docker
2️⃣ Create Flask App (app.py)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Secure Docker Deployment with Traefik!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
3️⃣ Requirements (requirements.txt)
Flask
4️⃣ Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
5️⃣ Traefik Configuration (traefik.yml)
global:
  checkNewVersion: true
  sendAnonymousUsage: false

entryPoints:
  web:
    address: ":80"
  websecure:
    address: ":443"

providers:
  docker:
    exposedByDefault: false

certificatesResolvers:
  myresolver:
    acme:
      email: your-email@example.com
      storage: acme.json
      httpChallenge:
        entryPoint: web
6️⃣ Docker Compose
services:
  traefik:
    image: traefik:v2.9
    command:
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.myresolver.acme.email=your-email@example.com"
      - "--certificatesresolvers.myresolver.acme.storage=/letsencrypt/acme.json"
      - "--certificatesresolvers.myresolver.acme.httpChallenge.entryPoint=web"
    ports:
      - "80:80"
      - "443:443"
      - "8081:8080"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
      - "./letsencrypt:/letsencrypt"

  web:
    build: .
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.web.rule=Host(`ashishdevops.online`)"
      - "traefik.http.routers.web.entrypoints=websecure"
      - "traefik.http.routers.web.tls.certresolver=myresolver"
      - "traefik.http.middlewares.auth.basicauth.users=admin:$$apr1$$TYHtefn8$$rP/tvtBDmbhtUB5.duNNt1"
      - "traefik.http.routers.web.middlewares=auth"
🔐 Generate Basic Auth Password
sudo apt install apache2-utils
echo $(htpasswd -nb admin mypassword) | sed -e s/\\$/\\$\\$/g
📂 Prepare SSL Storage
mkdir letsencrypt
touch letsencrypt/acme.json
chmod 600 letsencrypt/acme.json
▶️ Run the Application
docker compose up -d --build
🌐 Access
🔐 Application → https://ashishdevops.online
📊 Traefik Dashboard → http://localhost:8081
🌍 Domain Setup (Hostinger)

Configure DNS:

Type	Name	Value
A	@	YOUR_SERVER_IP
A	www	YOUR_SERVER_IP
🧪 Verification
ping ashishdevops.online
docker ps
docker logs <traefik-container>
🚨 Troubleshooting
Port already in use
sudo netstat -tulpn | grep :80
SSL not working
Domain not pointing correctly
Port 80 blocked
Running on local machine
Login not appearing

Ensure:

traefik.http.routers.web.middlewares=auth
🔐 Security Best Practices
Disable insecure dashboard (api.insecure=true)
Use strong passwords
Restrict ports using firewall
📈 Future Enhancements
CI/CD pipeline (GitHub Actions)
Monitoring (Prometheus + Grafana)
AWS EC2 deployment
Kubernetes Ingress
🧠 Resume Line

Built a secure Docker-based deployment using Traefik reverse proxy with automated SSL (Let’s Encrypt) and authentication middleware.

📌 Final Outcome

✔ HTTPS enabled
✔ Reverse proxy working
✔ Authentication secured
✔ Domain mapped correctly
✔ Production-ready setup

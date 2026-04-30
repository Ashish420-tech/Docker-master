🔹 Step 1: Clone Repository
git clone https://github.com/<your-username>/Docker-master.git
cd Docker-master/ci-cd-docker-app
🔹 Step 2: Build & Test Locally
docker build -t myapp .
docker run -p 5000:5000 myapp
🔹 Step 3: Push to Docker Hub
docker tag myapp <your-username>/myapp:latest
docker push <your-username>/myapp:latest
🔹 Step 4: Setup Jenkins
sudo systemctl start jenkins

Open:

http://localhost:8080
🔹 Step 5: Configure Jenkins
Create Pipeline Job
Use:
Pipeline script from SCM
Branch:
ci-cd-docker-app
Script Path:
Jenkinsfile
🔹 Step 6: Add Credentials

In Jenkins:

Manage Jenkins → Credentials

Add:

ID: docker-hub
Username + Password
🔹 Step 7: Setup Kubernetes
minikube start
kubectl get nodes
🔹 Step 8: Deploy Manually (First Test)
kubectl apply -f k8s/deployment.yaml
kubectl get pods
🔹 Step 9: Fix Jenkins Kubernetes Access
kubectl config view --raw > /tmp/kubeconfig

sudo mkdir -p /var/lib/jenkins/.kube
sudo mv /tmp/kubeconfig /var/lib/jenkins/.kube/config
sudo chown -R jenkins:jenkins /var/lib/jenkins/.kube
sudo systemctl restart jenkins
🔹 Step 10: Run Jenkins Pipeline
Click → Build Now
🔹 Step 11: Verify Deployment
kubectl get pods
kubectl get svc
🔹 Step 12: Access Application
minikube service myapp
🧠 Troubleshooting Guide
Issue	Fix
ErrImagePull	Check Docker image name
Jenkins Git error	Fix branch name
Docker permission denied	Add Jenkins to docker group
Kubernetes auth error	Fix kubeconfig
Port conflict	Use different port
🚀 Future Enhancements
Version tagging (no latest)
Helm charts
GitHub webhook → Jenkins trigger
Ingress controller
Monitoring (Prometheus + Grafana)
🎯 Outcome

✔ Fully automated CI/CD pipeline
✔ Docker image lifecycle managed
✔ Kubernetes deployment automated
✔ Real-world DevOps debugging handled

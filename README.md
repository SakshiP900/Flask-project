# Flask Kubernetes CI/CD Project

## Description
Multi-page Flask website deployed using Docker, Jenkins, and Kubernetes.

## Tech Stack
- Flask (Python)
- HTML, CSS
- MySQL (AWS RDS)
- Docker
- Jenkins
- Kubernetes (Minikube)

## CI/CD Flow
GitHub → Jenkins → Docker Hub → Kubernetes

## Run Locally
1. Clone the repo:
```bash
git clone https://github.com/SakshiP900/Flask-project.git
cd Flask-project

2. Build Docker image:
docker build -t flask-app:latest .

3. Run container:
docker run -d -p 30001:5000 \
  -e DB_HOST=<YOUR-RDS-ENDPOINT> \
  -e DB_NAME=<DB_NAME> \
  -e DB_USER=<DB_USER> \
  -e DB_PASSWORD=<DB_PASSWORD> \
  --name flask-demo \
  flask-app:latest

4. Access the app:
http://<EC2-PUBLIC-IP>:30001

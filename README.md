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
python app.py

## Build Docker Image
docker build -t flask-app .

## Kubernetes Deployment
kubectl apply -f k8s/

## Access App
minikube service flask-service


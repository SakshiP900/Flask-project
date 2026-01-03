pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/USERNAME/flask-k8s-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t username/flask-app:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push username/flask-app:latest'
            }
        }

        stage('Start Minikube') {
            steps {
                sh '''
                minikube start --driver=docker
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s/deployment.yml
                kubectl apply -f k8s/service.yml
                '''
            }
        }

        stage('Expose Service') {
            steps {
                sh '''
                minikube service flask-service --url
                '''
            }
        }
    }
}


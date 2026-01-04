pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "sakshiparadkar/flask-app:latest"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SakshiP900/Flask-project.git'
            }
        }

        stage('Docker Build & Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-hub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    script {
                        // Build Docker image
                        sh 'docker build -t flask-app:latest .'

                        // Login to Docker Hub
                        sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'

                        // Tag and push image
                        sh "docker tag flask-app:latest $DOCKER_IMAGE"
                        sh "docker push $DOCKER_IMAGE"
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(
                    credentialsId: 'kubeconfig-credentials',
                    variable: 'KUBECONFIG_FILE'
                )]) {
                    script {
                        // Deploy using kubeconfig secret
                        sh """
                        export KUBECONFIG="\$KUBECONFIG_FILE"
                        kubectl apply -f k8s/db-secret.yml
                        kubectl apply -f k8s/deployment.yml
                        kubectl apply -f k8s/service.yml
                        kubectl rollout restart deployment flask-app
                        """
                    }
                }
            }
        }

    }

    post {
        success {
            echo "Flask app deployment succeeded!"
        }
        failure {
            echo "Flask app deployment failed!"
        }
    }
}

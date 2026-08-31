pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-cicd-app .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run -d --name test-container -p 5000:5000 devops-cicd-app'
                sh 'sleep 5'
                sh 'curl http://localhost:5000/health'
                sh 'docker stop test-container'
                sh 'docker rm test-container'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment stage will be configured with AWS EC2.'
            }
        }
    }
}

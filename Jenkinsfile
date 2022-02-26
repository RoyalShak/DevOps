pipeline {
    agent any
    stages {
        stage('Checkout') { 
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RoyalShak/DevOps1411.git']]])
            }
        }
        stage('Build') {
            steps {
                bat 'docker build -t royalshakdockerfile:latest .'
            }
        }
        stage('Run') {
            steps {
                bat 'docker compose up -d'
            }
        }
        stage('Test') {
            steps {
                bat 'pip install selenium'
                bat 'python e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                bat 'docker-compose stop'
                bat 'docker tag royalshakdockerfile royalshak/royalshakdockerfile:latest'
                bat 'docker push royalshak/royalshakdockerfile:latest'
            }
        }
        
    }
}
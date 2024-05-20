pipeline {
    agent any

    stages {
        stage('Environment setup'){
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                sh 'ruff check'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover -s tests -p "test_*.py"'
                sh 'deactivate'
            }
        }
        stage ('Stop multi-container') {
            steps {
                sh 'docker compose down'
            }
        }
        stage('Run multi-container') {
            steps {
                sh 'docker compose up -d --build'
            }
        }
    }
}
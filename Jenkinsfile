pipeline {
    agent any

    stages {
        stage('Environment setup'){
            steps {
                sh 'python3 -m venv venv'
                sh '''
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Lint') {
            steps {
                sh '''
                    . venv/bin/activate
                    sh 'ruff check'
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m unittest discover -s tests -p "test_*.py"
                '''
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
pipeline {
    agent any

    stages {
        stage('Environment setup') {
            steps {
                script {
                    sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt
                        deactivate
                    '''
                }
            }
        }
        stage('Lint') {
            steps {
                script {
                    sh '''
                        source venv/bin/activate
                        ruff check
                        deactivate
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh '''
                        source venv/bin/activate
                        python -m unittest discover -s tests -p "test_*.py"
                        deactivate
                    '''
                }
            }
        }
        stage('Stop multi-container') {
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

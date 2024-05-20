pipeline {
    agent any

    stages {
        stage('Environment setup') {
            steps {
                script {
                    // Crear el entorno virtual y activar
                    sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt
                        pip freeze
                        deactivate
                    '''
                }
            }
        }
        stage('Lint') {
            steps {
                script {
                    // Activar el entorno virtual y ejecutar lint
                    sh '''
                        source venv/bin/activate
                        pip freeze
                        ruff check
                        deactivate
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Activar el entorno virtual y ejecutar pruebas
                    sh '''
                        source venv/bin/activate
                        pip freeze
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

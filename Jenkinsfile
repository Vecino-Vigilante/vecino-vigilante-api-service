pipeline {
    agent any

    environment {
        MYSQL_ROOT_PASSWORD = credentials('mysql-root-password')
        MYSQL_DATABASE = 'vecino-vigilante-db'
        MYSQL_USER = 'vv-user'
        MYSQL_PASSWORD = credentials('mysql-password')

        AWS_S3_REGION = 'us-east-2'
        AWS_S3_BUCKET_NAME = 'vecino-vigilante'
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')

        JWT_SECRET_KEY = credentials('jwt-secret-key')
        JWT_ALGORITHM = 'HS256'
    }

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
        stage('Create .env file') {
            steps {
                script {
                    sh '''
                        cat <<EOF > .env
                        MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
                        MYSQL_DATABASE=${MYSQL_DATABASE}
                        MYSQL_USER=${MYSQL_USER}
                        MYSQL_PASSWORD=${MYSQL_PASSWORD}

                        AWS_S3_REGION=${AWS_S3_REGION}
                        AWS_S3_BUCKET_NAME=${AWS_S3_BUCKET_NAME}
                        AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
                        AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}

                        JWT_SECRET_KEY=${JWT_SECRET_KEY}
                        JWT_ALGORITHM=${JWT_ALGORITHM}
                        EOF
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

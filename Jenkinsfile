pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv jenkins_venv
                    . jenkins_venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Pytest') {
            steps {
                sh '''
                    . jenkins_venv/bin/activate
                    python -m pytest -v
                '''
            }
        }

        stage('Code Coverage') {
            steps {
                sh '''
                    . jenkins_venv/bin/activate
                    python -m pytest --cov=ACEest_Fitness --cov-report=term-missing
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t aceest-fitness:${BUILD_NUMBER} .'
            }
        }
    }

    post {
        success {
            echo 'ACEest Fitness CI Pipeline completed successfully'
        }

        failure {
            echo 'ACEest Fitness CI Pipeline failed'
        }
    }
}

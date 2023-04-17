pipeline {
    agent any

    environment {
    }

    stages {
        stage('Checkout') {
            steps {
                git 'git@github.com:kumar4world/Date_Ranges.git'
            }
        }

        stage('Build') {
            steps {
                sh 'cd Date_Ranges'
                sh 'python3 manage.py collectstatic'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 manage.py test'
            }
        }

        stage('Package') {
            steps {
                sh 'python3 setup.py sdist'
                archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
            }
        }
    }

    post {
        always {
            junit 'test-reports/**/*.xml'
        }
    }
}


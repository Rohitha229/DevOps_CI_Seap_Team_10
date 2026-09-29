pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\Rohitha B\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest'
            }
        }
    }

    post {
        success {
            echo 'CI Build Successful - All tests passed.'
        }
        failure {
            echo 'CI Build Failed - Check the console output.'
        }
    }
}

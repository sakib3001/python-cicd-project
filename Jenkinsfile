pipeline {
    agent any 
    
    // Added some options
    options {
        timeout(time: 1, unit: 'HOURS')  // Corrected time value (should be an integer)
        retry(3)  // Retry 3 times
        skipDefaultCheckout()  // Skips the default Git checkout
    }

    environment {
        HOMEE = "Boom"
    }

    stages {
        stage('Git Checkout') {
            steps {
                git(url: 'https://github.com/sakib3001/python-cicd-project.git', branch: 'main')  // Fixed parameter spacing
            }
        }
        stage('Build') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'  // Python dependency installation
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/'  // Running tests using pytest
            }
        }
    }
}

pipeline {
    agent any 
    
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
                git(url: 'https://github.com/sakib3001/python-cicd-project.git', branch: 'main')
            }
        }
        stage('Install Poetry') {
            steps {
                sh '''
                    curl -sSL https://install.python-poetry.org | python3 -
                    export PATH="$HOME/.local/bin:$PATH"
                '''
            }
        }
        stage('Build') {
            steps {
                sh '''
                export PATH="$HOME/.local/bin:$PATH"
                poetry install
                poetry export --without-hashes -f requirements.txt > requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh 'poetry run pytest tests/'  
            }
        }
    }
}

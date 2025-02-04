pipeline {
    agent any 

    options {
        timeout(time: 1, unit: 'HOURS')  
        // retry(3)  
        skipDefaultCheckout()  // Skips the default Git checkout
    }

    environment {
        // Add Poetry's bin directory to the PATH
        PATH = "$HOME/.local/bin:$PATH"
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
                    poetry self add poetry-plugin-export
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                    poetry install
                    poetry export --without-hashes -f requirements.txt > requirements.txt
                '''
            }
        }

        stage('Test and Lint') {
            parallel {
                stage('Lint') {
                    steps {
                        sh '''
                            poetry run flake8 .
                        '''
                    }
                }
                stage('Test') {
                    steps {
                        sh '''
                            poetry run pytest tests/
                        '''
                    }
                }
            }
        }
    }
}
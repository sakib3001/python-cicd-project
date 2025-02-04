pipeline {
    agent any 

    options {
        timeout(time: 1, unit: 'HOURS')  // Corrected time value (should be an integer)
        // retry(3)  // Retry 3 times
        skipDefaultCheckout()  // Skips the default Git checkout
    }

    environment {
       PATH_DIR = "$HOME/.local/bin:$PATH"
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
                    export ${PATH_DIR}
                    poetry self add poetry-plugin-export
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                    export ${PATH_DIR}
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
                            export ${PATH_DIR}
                            poetry run flake8 .
                        '''
                    }
                }
                stage('Test') {
                    steps {
                        sh '''
                            export ${PATH_DIR}
                            poetry run pytest tests/
                        '''
                    }
                }
            }
        }
    }
}
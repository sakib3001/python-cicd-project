pipeline {
    agent any 

    options {
        timeout(time: 1, unit: 'HOURS')  
        // retry(3)  // Uncomment if you want to retry failed builds
        skipDefaultCheckout()  // Skips the default Git checkout
    }

    tools {
        dockerTool "docker"
    }

    environment {
        // Add Poetry's bin directory to the PATH
        PATH = "$HOME/.local/bin:$PATH"
        IMAGE_NAME = "webee-app" // Name of the Docker image
        IMAGE_REGISTRY = "xops2025" // Docker registry (e.g., Docker Hub, private registry)
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

        stage('File-system Scanning: Trivy') {
            steps {
                sh '''
                    trivy fs --format table -o trivy-fs-report.html .
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

        stage('Image Building') {
            steps {
                sh '''
                    docker build -t $IMAGE_NAME:$BUILD_NUMBER .
                    docker images
                    docker tag $IMAGE_NAME:$BUILD_NUMBER $IMAGE_REGISTRY/$IMAGE_NAME:$GIT_COMMIT
                '''
            }
        }

        stage('Image Scanning: Trivy') {
            steps {
                sh '''
                    trivy image --format table -o trivy-image-report.html $IMAGE_REGISTRY/$IMAGE_NAME:$GIT_COMMIT
                '''
            }
        }

        stage('Image Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-creds', passwordVariable: 'PASS', usernameVariable: 'USR')]) {
                    sh '''
                        docker login -u ${USR} -p ${PASS}
                        docker push $IMAGE_REGISTRY/$IMAGE_NAME:$GIT_COMMIT
                    '''
                }
            }
        }
    }
}
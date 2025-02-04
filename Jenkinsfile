pipeline {
    agent any 
    
    environment {
        HOMEE = "Boom"
    }

    stages {  
        stage('Git Checkout') {
            steps {
                git(url: 'https://github.com/sakib3001/python-cicd-project.git',branch: 'main')
            }
        }
        stage('Test') {
            steps {
                echo "My 1st Test! ${HOMEE}"
            }
        }
    }
    
}

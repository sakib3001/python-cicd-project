pipeline {
    agent any 
    
    // Added some options
    options{
      timeout(time:'1',unit: 'HOUR')
      retry(3)
      skipDefaultCheckout()
    } 

    environment {
        HOMEE = "Boom"
    }

    stages {  
        stage('Git Checkout') {
            steps {
                git(url: 'https://github.com/sakib3001/python-cicd-project.git',branch: 'main')
            }
        }
        stage('Build') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
    
}

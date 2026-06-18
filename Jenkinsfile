pipeline {
agent any

stages {

    stage('Checkout') {
        steps {
            sh 'ls -la'
        }
    }

    stage('Install Dependencies') {
        steps {
            sh '''
                pip3 install -r requirements.txt
            '''
        }
    }

    stage('Train Model') {
        steps {
            sh '''
                python3 train.py
            '''
        }
    }

    stage('Build Docker Image') {
        steps {
            sh '''
                docker build -t salary-predictor:v1 .
            '''
        }
    }

    stage('Verify Image') {
        steps {
            sh '''
                docker images | grep salary-predictor
            '''
        }
    }
}

post {
    success {
        echo 'MLOps Pipeline Completed Successfully'
    }
    failure {
        echo 'Pipeline Failed'
    }
}

}

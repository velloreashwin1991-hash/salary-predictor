pipeline {
agent any

stages {

    stage('Checkout') {
        steps {
            sh 'ls -la'
        }
    }

    stage('Create Python Environment') {
        steps {
            sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
            '''
        }
    }

    stage('Train Model') {
        steps {
            sh '''
                . venv/bin/activate
                python train.py
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

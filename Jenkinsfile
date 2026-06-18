pipeline {
agent any

stages {

    stage('Checkout') {
        steps {
            echo 'Git checkout successful'
        }
    }

    stage('Train Model') {
        steps {
            sh '''
            docker run --rm \
            -v $(pwd):/app \
            -w /app \
            python:3.14 \
            sh -c "pip install -r requirements.txt && python train.py"
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
}

}

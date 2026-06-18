pipeline {
agent any

stages {

    stage('Check Files') {
        steps {
            sh '''
                pwd
                ls -la
            '''
        }
    }

    stage('Train Model') {
        steps {
            sh '''
                docker run --rm \
                -v "$WORKSPACE:/app" \
                -w /app \
                python:3.14 \
                sh -c "pip install -r requirements.txt && python train.py"
            '''
        }
    }

    stage('Verify Model') {
        steps {
            sh '''
                ls -la
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

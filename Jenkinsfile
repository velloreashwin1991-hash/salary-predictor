pipeline {
agent any

stages {

    stage('Check Files') {
        steps {
            sh '''
                echo "Current Workspace:"
                pwd

                echo "Files:"
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
                sh -c "pwd && ls -la && pip install -r requirements.txt && python train.py"
            '''
        }
    }

    stage('Verify Model') {
        steps {
            sh '''
                echo "Workspace after training:"
                ls -la
            '''
        }
    }

    stage('Build Docker Image') {
        steps {
            sh '''
                docker build -t salary-predictor:v1 -f dockerfile .
            '''
        }
    }

    stage('Verify Docker Image') {
        steps {
            sh '''
                docker images | grep salary-predictor || true
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

    always {
        echo 'Pipeline Finished'
    }
}

}

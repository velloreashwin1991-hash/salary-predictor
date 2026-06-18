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
    stage('Run Docker Container') {
    steps {
        sh '''
            docker rm -f salary-predictor || true
            docker run -d \
            --name salary-predictor \
            -p 5000:5000 \
            salary-predictor:v1
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

pipeline {
agent any

environment {
    IMAGE_NAME = "salary-predictor:v1"
    CONTAINER_NAME = "salary-predictor"
}

stages {

    stage('Checkout') {
        steps {
            sh '''
                echo "Workspace:"
                pwd
                ls -la
            '''
        }
    }

    stage('Create Python Environment') {
        steps {
            sh '''
                python3 -m venv venv
                ./venv/bin/pip install --upgrade pip
                ./venv/bin/pip install -r requirements.txt
            '''
        }
    }

    stage('Train Model') {
        steps {
            sh '''
                ./venv/bin/python train.py
            '''
        }
    }

    stage('Build Docker Image') {
        steps {
            sh '''
                docker build -t ${IMAGE_NAME} .
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

    stage('Run Docker Container') {
        steps {
            sh '''
                docker rm -f ${CONTAINER_NAME} || true

                docker run -d \
                --name ${CONTAINER_NAME} \
                -p 5000:5000 \
                ${IMAGE_NAME}
            '''
        }
    }

    stage('Verify Container') {
        steps {
            sh '''
                docker ps
                docker logs ${CONTAINER_NAME} || true
            '''
        }
    }

    stage('Deploy to Kubernetes') {
        steps {
            sh '''
                if command -v kubectl >/dev/null 2>&1; then
                    kubectl apply -f deployment.yaml
                    kubectl get pods
                else
                    echo "kubectl not installed. Skipping Kubernetes deployment."
                fi
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
        echo 'Pipeline Execution Finished'
    }
}

}

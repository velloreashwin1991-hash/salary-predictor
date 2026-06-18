pipeline {
    agent any

    stages {
        stage('Check Files') {
            steps {
                sh '''
                    echo "Current Directory:"
                    pwd

                    echo "Files:"
                    ls -la

                    echo "Looking for requirements.txt"
                    find . -name "requirements.txt"
                '''
            }
        }
    }
}

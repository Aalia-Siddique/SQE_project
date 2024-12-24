pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Aalia-Siddique/SQE_project'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // For Windows, use bat instead of sh
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run Tests') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    script {
                        // For Windows, use bat instead of sh
                        bat 'pytest --junitxml=test-results.xml'
                    }
                }
            }
        }
    }
   post {
    always {
        script {
            if (fileExists('test-results.xml') && readFile('test-results.xml').trim()) {
                junit 'test-results.xml'
            } else {
                echo "No test results found."
            }
        }
    }
}
}

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
                    // Install dependencies using pip
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run Tests') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    script {
                        // Run pytest on the 'tests/' folder and save the results to 'test-results.xml'
                        bat 'pytest tests/ --junitxml=test-results.xml'
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                // Check if 'test-results.xml' exists and contains results
                if (fileExists('test-results.xml') && readFile('test-results.xml').trim()) {
                    junit 'test-results.xml'  // Publish the test results to Jenkins
                } else {
                    echo "No test results found."
                }
            }
        }
    }
}

pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
         stage('Clone repository') { 
            steps { 
                script{
                checkout scm
                }
            }
        }

        stage('Build') { 
            steps { 
                script{
                 app = docker.build("underwater")
                }
            }
        }
        stage('Test'){
            steps {
                 echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                script{
                        docker.withRegistry('https://953105634563.dkr.ecr.eu-north-1.amazonaws.com/jenkins_test', 'ecr:eu-north-1:aws-credentials') {
                    app.push("${env.BUILD_NUMBER}")
                    app.push("latest")
                    }
                }
            }
        }
    }
}
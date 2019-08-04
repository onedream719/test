import sys

pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                print(sys.path)
            }
        }
        stage('Test') { 
            steps {
                sh "echo Test" 
            }
        }
        stage('Deploy') { 
            steps {
                sh "echo Deploy"  
            }
        }
    }
}

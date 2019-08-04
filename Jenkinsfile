
pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                step{
                    println 'step1'
                }
                step{
                    println 'step2'
                }
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

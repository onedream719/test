
pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                step('step1'){
                    println 'step1'
                }
                step('step2'){
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

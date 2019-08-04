
pipeline {
   agent {
        node {
            label ‘master’
            customWorkspace "${env.JOB_NAME}/${env.BUILD_NUMBER}"
        }
    }

    stages {
        stage('Build') { 
            steps {
                println 'build'
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

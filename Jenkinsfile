pipeline {
   agent any
   environment {
       registry = 'deepanmurugan/python'
       registryCredential = 'dockerhub'
       dockerImage = ''
   }
   stages {
       stage('Build') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                }
            } 
        }
       stage('Test') {
           steps {                
               sh 'echo "Testing the docker built image"'
           }
       }
       stage('Publish') {
           steps{
               script {
                     docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                   }
               }
           }
       }
       stage ('Deploy') {
           steps {
               script{
                   def image_id = registry + ":$BUILD_NUMBER"
                   sh "ansible-playbook  playbook.yml --extra-vars \"image_id=${image_id}\""
               }
           }
       }
   }
}

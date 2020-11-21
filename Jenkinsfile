pipeline {
   agent any
   environment {
       app = 'shopping_app'
       service = 'service1'
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
       stage('Pull Playbook Repo') {
        steps {
          dir('/tmp/ansible-playbooks/') {
          checkout poll: false, scm: [$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [[$class: 'CloneOption', noTags: false, reference: '', shallow: false, timeout: 10]], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'github_repo', url: 'https://github.com/deepanmurugan/Ansible_Playbook.git']]]
          }
          }
       }
       stage ('Deploy') {
           steps {
           dir('/tmp/ansible-playbooks/') {
               script{
                   def image_id = registry + ":$BUILD_NUMBER"
                   sh "ansible-playbook deploy_k8s.yml --extra-vars \"image_id=${image_id} app_name=${app} service_name=${service}\""
               }
           }
           }
       }
   }
}

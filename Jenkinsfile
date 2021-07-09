         
pipeline {
    agent any
    stages {

        

        stage('Install Dependencies'){
            steps{

                dir("scripts") {
                        sh 'chmod +x dependencies.sh'}
                
                sh './scripts/dependencies.sh'
            }
        }
      
        stage('Test'){
            steps{

                dir("scripts") {
                            sh 'chmod +x test.sh'}
                    
                    sh './scripts/test.sh'  
                
            }
        }
         
        
        stage('Build'){
            steps{
                sh 'sudo docker-compose build'
               
            }
        } 
        stage('Configure - Ansible'){
            steps{
                sh 'ansible-playbook -i inventory.yaml playbook.yaml'
               
            }
        } 
        
        

        stage('Deploy'){
            steps{
                sh 'sudo docker-compose push'
                sh 'scp docker-compose.yaml jenkins@35.184.174.59:docker-compose.yaml'
                sh "ssh 35.184.174.59 sudo docker stack deploy --compose-file docker-compose.yaml flaskapp"
               
            }
        } 

    }
}

               
      

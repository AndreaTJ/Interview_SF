         
pipeline {
    agent any
    stages {
      
        stage('Test'){
            steps{
                /*
                dir("service1") {
                        sh "python3 -m pytest --cov=app"
                }*/
               
                dir("service2") {
                        sh "python3 -m pytest --cov=app"
                }
                 dir("service3") {
                        sh "python3 -m pytest --cov=app"
                }
                 dir("service4") {
                        sh "python3 -m pytest --cov=app"
                }
            }
        }
         
        
        stage('Build'){
            steps{
                sh 'docker-compose build'
               
            }
        } 
        stage('Configure - Ansible'){
            steps{
                sh 'ansible-playbook -i inventory.yaml playbook.yaml'
               
            }
        } 
        

        stage('Deploy'){
            steps{
                sh 'scp docker-compose.yaml jenkins@35.188.151.251:docker-compose.yaml && docker-compose push'
                sh "ssh 35.188.151.251 docker stack deploy --compose-file docker-compose.yaml flaskapp"
               
            }
        } 
        
        stage('LoadBalancer'){
            steps{
                sh 'scp nginx/nginx.conf jenkins@34.122.221.134:nginx'
                sh "ssh jenkins@34.122.221.134 docker service rm nginx-loadbalancer"
                sh "ssh jenkins@34.122.221.134 docker service create -d -p 80:80 --name nginx-loadbalancer --mount type=bind,source=/home/jenkins/nginx.conf,target=/etc/nginx/nginx.conf nginx:alpine"
                sh "ssh jenkins@34.122.221.134 docker service update --replicas 4 nginx-loadbalancer"

            }
        }
    }
}

               
      

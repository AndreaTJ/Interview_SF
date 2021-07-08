# QA_Project2 - Travel Generator

The following document contains the breakdown of the development process of "Travel Generator".

## Requirements

The agreed requirements for this project are the following:

> The project needs to utilise the technologies discussed during the training modules: 

* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX

## My approach

To satisfy the requirements of this project, I developed an application that generates a random destination and budget for an imaginary trip this summer called “Travel Generator”. 


The application has been structured as follows

### Version 1

![https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/634671b492e22899c1379bf5bde21927/Screenshot_2021-03-01_at_23.51.30.png](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/634671b492e22899c1379bf5bde21927/Screenshot_2021-03-01_at_23.51.30.png)

**Service 2**

Generate a random response. Pick a destination from a list (randomly) and return it. This application uses port 5003.

**Service3**

Generate a random response. Pick a quote from a list (randomly) and return it. This application uses port 5003.

 
**Service4**

Service 4 receives the destination and budget for that trip.
If the length of the country is less than 6 characters, it will divide the budget money by 25 and add 1 unit. If the length is outside the range (0.7), then the money will be multiplied by 5. It returns the pair: country / budget after modifying the latter.
This application uses port 5004.

**Service1**

This service receives the destination / budget pair. After that, take two actions. It shows the user, the pair of values using a template based on Html / Jinja2 and saves both data in a database.
This application uses port 5000.


**User interface (V1):**

![https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/6776d273c3b6c487ea72d9bbc385d170/Screenshot_2021-03-02_at_01.32.12.png
](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/6776d273c3b6c487ea72d9bbc385d170/Screenshot_2021-03-02_at_01.32.12.png)


---

### Version 2	

**Service 2**

Generates a single value and returns it. This application uses port 5003.

**Service3**

Generate a random response. Pick a quote from a list other than version 1 and return it. This application uses port 5003.

![](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/25804054e2da8e22b111ecda286da732/Screenshot_2021-03-01_at_23.51.44.png)


 
**Service4**

Service 4 receives the destination and budget for that trip.
It will multiply the initial budget x10. Returns the pair: country / budget after modifying the latter.
This application uses port 5004.


**Service1**

This service receives the destination / budget pair. After that, take two actions. It shows the user, the pair of values using a template based on Html / Jinja2 and saves both data in a database. Certain colours have been modified. The most significant change is the colour of the background, which goes from white to orange.
This application uses port 5000.


**User interface (V2):**

![
https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/cbeb80812f5f38093e13c62d5abfb424/Screenshot_2021-03-01_at_23.52.44.png
](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/cbeb80812f5f38093e13c62d5abfb424/Screenshot_2021-03-01_at_23.52.44.png)


## Project Tracking 

A Trello Board has been used to keep a constant tracking of my activities, where I have been annotating the tasks derived from the creation of services and all significant changes, trying to emulate the Agile methodology at all times.

![](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/8df6407160560d016773309b602dfed2/Uno.png)

The appearance of the board, during development.

![](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/3ac20dca767afc58e51bb610a1f4d5d9/Progress.png)

The board has evolved as the development of the application did. Given the presence of blocks, I added a new tab called "Blocked" where the problems, that have needed investigation and a trial/error approach, are noted.

![](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/19ccd4fdc9d4ed0f16d46ac95ac8f8a6/Error.png)

The appearance of the board, at the end of development.

![](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/7881f5e8bffd3dad873c9cb377767cf9/Final.png)

# Database 

![](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/d86ba5903bf8cbb7f093ecf9e97bc71b/Screenshot_2021-03-01_at_23.39.43.png)

A table has been created with three fields: id, country (destination), and money (budget). Service number 1 will be in charge of Create, Read and Update records in the database.

A db managed database (GCP, SQL) has been used for this project.



## CI Pipeline (Diagram)

Once the bases of our project have been defined, we can start coding our application. This is when we start to go through our CI pipeline.

![](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/80c1285e0806bd3a0bdecfc697277920/Screenshot_2021-03-02_at_00.29.32.png)

The code is created by the developer (VSCode, Python, Flask) and tested using (Pytest and Unittest). To record and track any changes, we use a VSC and Github as a code hosting platform. After that, the CI server (Jenkins) handles all the construction, configuration, testing and automatic implementation of the application. Thanks to a webhook, Jenkins is able to detect any new changes in our repository.

After the automatic testing by the CI server, the images of our services are built and Ansible is launched, which is in charge of configuring the Master, Worker and Load Balancer. It will install the necessary dependencies to use Docker and Docker Swarm, which will allow us to deploy our application.

After the process is complete, a report is generated. However, if there has been a failure, the developer has been notified.

Based on a continuous deployment approach, the application is ready for the live environment.

During this process, each time the set of assigned tasks has been completed, we go back to the Backlog (Trello) to find out what our next task or set of tasks is.

## Pipeline Job

The pipeline follows has 5 stages for version 1 and 3 for version 2.


![](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/7b3688edc5b4a77fdc81bf72410c2ac9/V1.png)

### Testing

This is the first step in our pipeline, in this way, we make sure that the application passes the designed tests.

Two testing frameworks: Pytest and Unittest have been used in order to achieve the desired coverage level.

Service1 has been tested using the patch method (Unittest Mock, Python library). Since the object that would generate the actual request would be of type json, I have used the return_value.json.return_value attribute to simulate the expected result of the request.

![](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/e11b080171295bcf4e29503dc11a5bd9/T1_OK.png)

In this case, I have failed to show the test of service1. The service exhibits different behaviours in different VMs, so it requires a deeper investigation to know the causes.

![](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/3084c07b7cefc6d93dc30a88d35b4ca7/T1_fail.png)

Services 2 and 3 are both applications, consisting of a function that has been 100% tested.

![](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/f71b6016d5461486cef4c06c83393d24/t2.png)

![](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/6e6f110e1377c7671bc71bbcd592b921/T3.png)

To test service 4, we have used the patch (Unittest Mock) method as a decorator to alter the behaviour of "requests.get" and mock the response. We also gave it a mock object as a return value.
The percentage reached has been 90%. The untested function has been manually tested prior to application deployment.

![](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/f10aa15d1aca684af3fc110d338b8a8a/T4.png)

### Build

The next stage in the pipeline is: Build.
In this step, we will build the images of our 4 services. To do this, we will use Docker Compose (docker-compose build) which will create all the images in a single step. The specifications with which the images will be built are found in the Dockerfile of each application.

### Configure - Ansible

In this project we use Ansible as a configuration management tool.

Ansible will take care of:

- Install Docker in our Master VM, Worker VM and in the Load Balancer VM. All of them will need to be able to run docker to do their part in this project.

- It will also start the swarm on our Master machine and make the Worker join the swarm. In this way, we can use the Docker stack to deploy our application.

### Deploy

After the construction of images, they will be pushed to our registry, in this case, to our personal account in Docker Hub. After this, the deployment of our application will begin, starting with pulling the images from the repository. For the deployment we have made use of the Docker stack. Our node manager executes the command (docker stack deploy --compose-file docker-compose.yaml flaskapp) and with the help of our worker, deploys the application (Manager and worker are part of the same swarm).
During this process, replicas of the services will be created to ensure that the application is always available (redundancy and high availability).


### Load balancer

In this last step, we make sure our VM with Nginx as a service is doing the load balancer work. In this case, we use Nginx also as a reverse proxy for our application.

----
**For our second version**, the stages are reduced to three, to decrease the wait 
time for the deployment.

![](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/8890b7a005cd996bf8f3a17a9facf7e4/Screenshot_2021-03-01_at_20.42.39.png)
	
# Risk Assessment 


The following risk assessment identifies hazards and risk factors that could cause harm to the implementation of our services. I have listed the prevention measures I have used to control the risk when the hazard cannot be eliminated.

![](https://trello-attachments.s3.amazonaws.com/603d8d45a2a5d167bf6713b6/603d9493c064c46fb04f8e53/53e75cd2c5729fbd16e6504d5fedf8a7/Screenshot_2021-03-01_at_23.35.24.png)


# Further Improvements

Overall, this project was successful in creating 4 services and deploying them using Docker. However, there are a few improvements that I would like to implement:

- Testing: To get all the tests to work regardless of the machine they are on.
- Use frameworks like Bootstrap or Paper CSS to improve the final appearance.
- Use a second worker to improve redundancy and availability of services.
- Use Nexus as a repository manager.
- Add a button to refresh the result


# Acknowledgements

* Thanks to Ben Hesketh, Nathan Forester and Jay Grindrod for the time they spent helping me understand and correct my problems and concerns.
* Thanks to K.V and W.S for their patience and help.
* And thanks to F. Hidalgo for his emotional support.

# Autor
Andrea Torres-Jaramillo



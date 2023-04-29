#STEP 1 #Install Doker in AWS IDE Cloud9 Environment
sudo yum update -y
sudo yum install docker -y
curl -sfL https://get.k3s.io | sh -
docker version



#Step 2: Build Docker file for Boto3/Python

#Week 16 Project
#Build Dockerfile for Boto3/Python
#Use Ubuntu official image on DockerHub

#syntax-docker/Dockerfile
FROM ubuntu:22.04

#Install app dependencies
RUN apt-get update
RUN apt-get -y install python3-pip \
    && pip install boto3
    
ENTRYPOINT ["tail", "-f", "/dev.null'"]


#Step 3: Pull Ubuntu Docker official image & run the following command in the AWS CLI

#docker pull ubuntu

#Step 4: Download 3 repositories to local host
git clone <repo URL>
git clone https://github.com/Jleeluit/ubuntu-image.git
git clone https://github.com/Jleeluit/Ubuntu-runner-images.git
git clone https://github.com/Jleeluit/ubuntudocs-1.git

ls

#Step 5: Create 3 Containers with bind mount to a repository.
#Reposoritory Path

find $(pwd) -name <directory name>
find $(pwd) -name ubuntudocs-1
find $(pwd) -name ubuntu-image
find $(pwd) -name Ubuntu-runner-images

docker run -d -t --name <containerName> -v "$(pwd)"<repositoryName>:/<directory_name> <image_name>

docker run -d -t --name container1 -v "$(pwd)"ubuntudocs-1:/DockerProjectWeek16 ubuntu
docker run -d -t --name container2 -v "$(pwd)"ubuntu-image:/DockerProjectWeek16 ubuntu
docker run -d -t --name container3 -v "$(pwd)"Ubuntu-runner-images:/DockerProjectWeek16 ubuntu 

docker container ps


#Step 6: Inspect all 3 containers to check the mounts of the containers.
docker container inspect <containerName>

docker container inspect container1
docker container inspect container2
docker container inspect container3


#Step 7: Verify access to each repository directory by login into each container.

docker exec -it <container_name_or_id> bash

docker exec -it container1 bash
docker exec -it container2 bash
docker exec -it container3 bash

#To delete your containers run any one of the following commands
docker container rm <container_name>
docker container rm <container_ID>
docker container prune
#Update the System
sudo yum update -y

#Install Docker
sudo yum install docker -y

#Enable Docker
sudo systemctl enable docker

#Start Docker
sudo systemctl start docker

#Add our user to the docker group in each instance
sudo usermod -aG docker $USER

#Docker Version
sudo docker version
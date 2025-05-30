#!/bin/bash
# Script to set up an EC2 instance with Docker and Grafana

# Update the system
sudo yum update -y

# Install Docker
sudo yum install docker -y

# Start and enable Docker
sudo systemctl start docker
sudo systemctl enable docker

# Add user to Docker group (optional)
sudo usermod -aG docker $USER

# Verify Docker installation
docker --version

# Run Grafana in a Docker container
docker run -d -p 3000:3000 --name=grafana grafana/grafana

# Verify Grafana is running
docker ps

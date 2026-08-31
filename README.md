# devops-cicd-project
my 1st project



# 🚀 DevOps CI/CD Project

A simple Python Flask web application deployed on an AWS EC2 instance using Docker.

This project demonstrates the basic DevOps workflow:

**GitHub → AWS EC2 → Docker → Running Application**

---

## 📌 Project Objective

The objective of this project is to deploy a Python Flask application on an AWS EC2 instance using Docker.

The project covers:

- Git and GitHub
- Linux
- AWS EC2
- Docker
- Flask
- Basic application deployment

Jenkins will be integrated later to automate the CI/CD pipeline.

---

## 🏗️ Architecture

```text
                  GitHub Repository
                         |
                         | git clone
                         v
                  AWS EC2 Instance
                       Ubuntu
                         |
                         v
                  Docker Build
                         |
                         v
                Docker Image
                         |
                         v
                Docker Container
                         |
                         v
                    Port 5000
                         |
                         v
                  Web Browser
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| Flask | Web framework |
| Git | Version control |
| GitHub | Source code repository |
| Linux | EC2 server operating system |
| AWS EC2 | Cloud server |
| Docker | Application containerization |
| Docker Hub | Container image repository |
| Jenkins | CI/CD automation (upcoming) |

---

# 📁 Project Structure

```text
devops-cicd-project/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── README.md
```

### File Description

| File | Description |
|------|-------------|
| `app.py` | Python Flask application |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Instructions to build Docker image |
| `Jenkinsfile` | Jenkins pipeline configuration |
| `README.md` | Project documentation |

---

# ☁️ AWS EC2 Setup

## Step 1: Create EC2 Instance

Create an EC2 instance with the following configuration:

- AMI: Ubuntu Server 24.04 LTS
- Instance Type: `t2.micro` or `t3.micro`
- Storage: 8 GB
- Key Pair: Required for SSH access

---

## Step 2: Configure Security Group

Add the following inbound rules:

| Type | Port | Source |
|------|------|--------|
| SSH | 22 | My IP |
| HTTP | 80 | Anywhere |
| Custom TCP | 5000 | Anywhere |

Port `5000` is used by the Flask application.

> For production deployment, Nginx can be configured to expose the application through port 80 instead of directly exposing port 5000.

---

# 🔐 Connect to EC2

## Step 3: Connect using SSH

From Windows PowerShell:

```bash
ssh -i "your-key.pem" ubuntu@YOUR_EC2_PUBLIC_IP
```

Example:

```bash
ssh -i "devops-project.pem" ubuntu@13.234.XX.XX
```

After successful login:

```text
ubuntu@ip-172-31-xx-xx:~$
```

---

# 🐳 Docker Installation

## Step 4: Update Ubuntu

```bash
sudo apt update
```

---

## Step 5: Install Docker

```bash
sudo apt install docker.io -y
```

Check Docker installation:

```bash
docker --version
```

---

## Step 6: Start Docker

```bash
sudo systemctl enable --now docker
```

Check Docker service:

```bash
sudo systemctl status docker
```

---

## Step 7: Allow Ubuntu User to Run Docker

```bash
sudo usermod -aG docker $USER
```

Exit from the EC2 server:

```bash
exit
```

Reconnect to EC2:

```bash
ssh -i "your-key.pem" ubuntu@YOUR_EC2_PUBLIC_IP
```

Test Docker:

```bash
docker ps
```

Docker should now work without using `sudo`.

---

# 📦 Clone GitHub Repository

## Step 8: Install Git

Check whether Git is installed:

```bash
git --version
```

If Git is not installed:

```bash
sudo apt install git -y
```

---

## Step 9: Clone the Repository

```bash
git clone https://github.com/atulwale18/devops-cicd-project.git
```

Move into the project directory:

```bash
cd devops-cicd-project
```

Check project files:

```bash
ls
```

Expected output:

```text
Dockerfile
Jenkinsfile
README.md
app.py
requirements.txt
```

---

# 🐋 Build Docker Image

## Step 10: Build Docker Image

Inside the project directory:

```bash
docker build -t devops-cicd-app .
```

Check the Docker image:

```bash
docker images
```

Expected image:

```text
devops-cicd-app
```

---

# 🚀 Run Docker Container

## Step 11: Start the Container

```bash
docker run -d --name devops-app -p 5000:5000 devops-cicd-app
```

### Command Explanation

```text
docker run
```

Creates and starts a container.

```text
-d
```

Runs the container in detached/background mode.

```text
--name devops-app
```

Assigns a name to the container.

```text
-p 5000:5000
```

Maps EC2 port 5000 to the container's port 5000.

```text
devops-cicd-app
```

Specifies the Docker image to use.

---

# 🔍 Verify Container

## Step 12: Check Running Containers

```bash
docker ps
```

You should see:

```text
CONTAINER ID   IMAGE             PORTS
xxxxxxxx       devops-cicd-app   0.0.0.0:5000->5000/tcp
```

---

# 🌐 Access the Application

## Step 13: Open Application in Browser

Find the **Public IPv4 address** of your EC2 instance.

Example:

```text
13.234.XX.XX
```

Open:

```text
http://YOUR_EC2_PUBLIC_IP:5000
```

The application should display:

```text
Hello from my DevOps CI/CD Pipeline 🚀

Application deployed using Jenkins, Docker and AWS EC2.

Version: 1.0
```

---

# ❤️ Health Check

The application also provides a health-check endpoint.

Open:

```text
http://YOUR_EC2_PUBLIC_IP:5000/health
```

Expected response:

```json
{
    "application": "DevOps CI/CD Demo",
    "status": "healthy"
}
```

---

# 🔧 Useful Docker Commands

### Check running containers

```bash
docker ps
```

### Check all containers

```bash
docker ps -a
```

### Stop container

```bash
docker stop devops-app
```

### Start container

```bash
docker start devops-app
```

### Restart container

```bash
docker restart devops-app
```

### Remove container

```bash
docker rm -f devops-app
```

### Check Docker images

```bash
docker images
```

### Remove Docker image

```bash
docker rmi devops-cicd-app
```

### View container logs

```bash
docker logs devops-app
```

### Follow container logs

```bash
docker logs -f devops-app
```

---

# 🔄 Update Application

If changes are pushed to GitHub:

```bash
git pull
```

Rebuild the Docker image:

```bash
docker build -t devops-cicd-app .
```

Remove the old container:

```bash
docker rm -f devops-app
```

Start a new container:

```bash
docker run -d --name devops-app -p 5000:5000 devops-cicd-app
```

---

# 🔮 Future CI/CD Implementation

Jenkins will be integrated into the project to automate the deployment process.

The final architecture will be:

```text
Developer
    |
    v
GitHub
    |
    v
Jenkins
    |
    +------> Build
    |
    +------> Test
    |
    +------> Docker Build
    |
    +------> Push to Docker Hub
    |
    v
AWS EC2
    |
    v
Docker Container
    |
    v
Web Application
```

---

# 🎯 Final Project Goals

The complete project will demonstrate:

- Git version control
- GitHub repository management
- Linux server administration
- AWS EC2 deployment
- Docker image creation
- Docker container management
- Application deployment
- Jenkins CI/CD
- Automated deployment
- Docker Hub integration

---

# 👨‍💻 Author

**Atul Wale**

DevOps Engineer | AWS | Linux | Docker | Jenkins | Git

🚀 AWS VPC + RDS + Flask Application

A production-style AWS cloud deployment project demonstrating how to deploy a Python Flask web application on Amazon EC2, connect it securely to Amazon RDS MySQL, and monitor the infrastructure using Amazon CloudWatch.

---

🏗️ Architecture

                         🌐 Internet
                              │
                              ▼
                  ┌──────────────────────┐
                  │  Internet Gateway    │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │    Public Subnet     │
                  │                      │
                  │  🖥️ Amazon EC2       │
                  │  🐍 Flask Application │
                  │  Port: 5000          │
                  └──────────┬───────────┘
                             │
                        MySQL : 3306
                             │
                             ▼
                  ┌──────────────────────┐
                  │   Private Subnet     │
                  │                      │
                  │  🗄️ Amazon RDS       │
                  │     MySQL Database   │
                  └──────────────────────┘


                    ☁️ CloudWatch
                          │
                          ▼
                   EC2 Monitoring

🔄 Request Flow

User
 │
 ▼
Internet Gateway
 │
 ▼
Public Subnet
 │
 ▼
EC2 → Flask Application
 │
 │ MySQL :3306
 ▼
Private Subnet
 │
 ▼
RDS MySQL

---

🛠️ Technologies Used

Technology| Purpose
☁️ AWS VPC| Network isolation
🖥️ Amazon EC2| Flask application server
🗄️ Amazon RDS| Managed MySQL database
📊 Amazon CloudWatch| Monitoring
🌐 Internet Gateway| Internet connectivity
🔐 Security Groups| Network security
🐍 Python| Application development
🌶️ Flask| Web framework
🐬 MySQL| Database
🐧 Linux / Ubuntu| Server environment
🔧 Git & GitHub| Version control

---

📌 Project Features

- ✅ Created a custom AWS VPC
- ✅ Created public and private subnets
- ✅ Configured an Internet Gateway
- ✅ Configured public and private route tables
- ✅ Deployed a Flask application on EC2
- ✅ Created a MySQL database using Amazon RDS
- ✅ Connected Flask application to RDS
- ✅ Secured database access using Security Groups
- ✅ Configured EC2 monitoring using CloudWatch

---

🔐 Security Design

The architecture uses separate Security Groups for EC2 and RDS.

🖥️ EC2 Security Group

Protocol| Port| Source| Purpose
SSH| "22"| My IP| Server administration
TCP| "5000"| Internet| Flask application

🗄️ RDS Security Group

Protocol| Port| Source| Purpose
MySQL| "3306"| EC2 Security Group| Database connection

«🔒 The RDS database is placed in a private subnet and only accepts MySQL traffic from the EC2 Security Group.»

---

📁 Project Structure

aws-vpc-rds-flask-project/
│
├── 📄 app.py
├── 📄 requirements.txt
├── 📁 templates/
│   └── 📄 home.html
├── 📄 .gitignore
└── 📄 README.md

---

🚀 Installation & Deployment

1️⃣ Clone the Repository

git clone https://github.com/tahir1111-hub/aws-vpc-rds-flask-project.git

cd aws-vpc-rds-flask-project

2️⃣ Create a Python Virtual Environment

python3 -m venv venv

source venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Configure the Database

Create a local "config.py" file and add your RDS connection details:

MYSQL_CONFIG = {
    "host": "YOUR_RDS_ENDPOINT",
    "user": "YOUR_RDS_USERNAME",
    "password": "YOUR_RDS_PASSWORD",
    "port": 3306
}

«⚠️ Never commit "config.py" containing real database credentials to GitHub.»

Add it to ".gitignore":

config.py
venv/
__pycache__/
*.pyc

5️⃣ Run the Flask Application

python app.py

6️⃣ Access the Application

Open:

http://YOUR_EC2_PUBLIC_IP:5000

---

☁️ AWS Infrastructure

The project demonstrates the following AWS networking architecture:

AWS VPC
│
├── 🌐 Public Subnet
│   └── EC2
│       └── Flask Application
│
├── 🔒 Private Subnet
│   └── RDS MySQL
│
├── 🌐 Internet Gateway
│
├── 🛣️ Route Tables
│   ├── Public Route Table
│   └── Private Route Table
│
└── 🔐 Security Groups
    ├── EC2 Security Group
    └── RDS Security Group

---

📊 Monitoring

Amazon CloudWatch is used to monitor the EC2 instance.

Example metrics include:

EC2
 │
 └── CloudWatch
      ├── CPU Utilization
      ├── Network Traffic
      ├── Instance Status
      └── Monitoring Metrics

---

🎯 Project Goal

The goal of this project is to understand how a basic web application can be deployed on AWS using a secure and structured cloud architecture.

This project demonstrates practical knowledge of:

- AWS networking
- VPC architecture
- EC2 deployment
- RDS database connectivity
- Security Groups
- Linux server administration
- Python Flask
- CloudWatch monitoring
- Git & GitHub

---

👨‍💻 Author

Tahir

"BCA Student | Aspiring Cloud & DevOps Engineer"

---

⭐ If you found this project useful, consider giving the repository a star!

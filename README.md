# aws-vpc-rds-flask-project
aws-vpc-rds-flask-project 
# AWS VPC + EC2 + RDS + Flask + CloudWatch

A hands-on AWS project demonstrating how to deploy a Flask application on an EC2 instance, connect it securely to an Amazon RDS MySQL database inside a private subnet, and monitor the EC2 instance using Amazon CloudWatch.

## 🏗️ Architecture

```text
                         Internet
                            │
                            ▼
                   ┌─────────────────┐
                   │ Internet Gateway│
                   └────────┬────────┘
                            │
                            ▼
                   ┌─────────────────┐
                   │   Public Subnet │
                   │                 │
                   │  EC2 Instance   │
                   │  Flask App      │
                   │  Port: 5000     │
                   └────────┬────────┘
                            │
                       MySQL :3306
                            │
                            ▼
                   ┌─────────────────┐
                   │  Private Subnet │
                   │                 │
                   │   RDS MySQL     │
                   │   Database      │
                   └─────────────────┘

                     CloudWatch
                         │
                         ▼
                  EC2 Monitoring


🚀## Technologies Used
AWS VPC
Amazon EC2
Amazon RDS (MySQL)
Amazon CloudWatch
Internet Gateway
Public & Private Subnets
Route Tables
Security Groups
Python
Flask
MySQL
Git & GitHub
Linux / Ubuntu

📌 ##Project Features
Created a custom AWS VPC
Created public and private subnets
Configured Internet Gateway
Configured public and private route tables
Deployed Flask application on EC2
Created MySQL database using Amazon RDS
Connected EC2 Flask application to RDS
Secured RDS access using Security Groups

🔐 ##Security Design

The project uses separate Security Groups for EC2 and RDS.

EC2 Security Group
Protocol	Port	Source
SSH	22	My IP
TCP	5000	Internet

| Protocol | Port | Source             |
| -------- | ---: | ------------------ |
| MySQL    | 3306 | EC2 Security Group |


##
aws-vpc-rds-flask-project/
│
├── app.py
├── requirements.txt
├── templates/
│   └── home.html
├── .gitignore
└── README.md


##1. Clone the repository

git clone https://github.com/tahir1111-hub/aws-vpc-rds-flask-project.git
cd aws-vpc-rds-flask-project


##2. Create a Python virtual environment

python3 -m venv venv
source venv/bin/activate

##3. Install dependencies

pip install -r requirements.txt

##4. Configure the database

##Create a local config.py file and add your RDS connection details:
MYSQL_CONFIG = {
    'host': 'YOUR_RDS_ENDPOINT',
    'user': 'YOUR_RDS_USERNAME',
    'password': 'YOUR_RDS_PASSWORD',
    'port': 3306
}

##5. Run the Flask application

python app.py

##6. The application run on

http://0.0.0.0:5000

🎯 Project Goal

The goal of this project is to understand how a basic web application can be deployed on AWS using a secure and structured cloud architecture.

👨‍💻 Author

Tahir

BCA Student | Aspiring Cloud & DevOps Engineer


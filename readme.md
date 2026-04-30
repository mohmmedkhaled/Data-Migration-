E-Commerce Data Warehouse Project: Sales Analytics

📌 Project Overview

This project demonstrates an End-to-End Data Engineering Pipeline for an e-commerce platform. The goal is to migrate raw operational data (Olist Dataset) into a centralized PostgreSQL Database hosted on Google Cloud Platform (GCP). 

🏗 Architecture & Tech Stack
Infrastructure as Code (IaC): Terraform (GCP Provider).

Database: Cloud SQL (PostgreSQL 15).

Orchestration/ETL: Python (Pandas, SQLAlchemy).

Cloud Provider: Google Cloud Platform (GCP).

sales-analytics-project/
├── terraform/          # Infrastructure configuration (Main, Variables, tfvars)
├── data/               # Raw CSV datasets (Olist E-commerce)
├── etl/                # Python scripts for data extraction and loading




🚀 Implementation Phases
Phase 1: Infrastructure Setup (Terraform)
Automated the provisioning of the cloud environment on GCP:

Provisioned a Cloud SQL Instance running PostgreSQL.

Configured Network Authorization and IAM Service Accounts for secure access.

Managed sensitive credentials using terraform.tfvars (excluded from version control).




Phase 2: Data Extraction & Loading (ETL)
Developed a Python-based ETL pipeline to move data from local CSV files to the Cloud:

Extraction: Reading multi-table datasets (Customers, Orders, Products, etc.).

Loading: Utilizing SQLAlchemy to batch-load data into a "Landing Zone" (Raw Tables) within PostgreSQL.

Validation: Implemented error handling for connection strings and file integrity.




🛠️ How to Run
1.Initialize Infrastructure:
cd terraform
terraform init
terraform apply


2.Run ETL Pipeline:
cd etl
pip install -r requirements.txt
python load_raw_data.py


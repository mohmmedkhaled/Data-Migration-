# terraform/main.tf

provider "google" {
  credentials = file("gcp-key.json")  
  project = var.project_id
  region  = "asia-south1"
}

resource "google_sql_database_instance" "postgres_instance" {
  name             = "sales-analytics-db"
  database_version = "POSTGRES_15"
  region           = "asia-south1" 

  settings {
    tier = "db-f1-micro" 
    ip_configuration {
      ipv4_enabled = true
      
      authorized_networks {
        name  = var.network_name
        value = var.network_cidr 
      }
    }
  }
}

resource "google_sql_database" "database" {
  name     = "sales_dw"
  instance = google_sql_database_instance.postgres_instance.name
}

resource "google_sql_user" "users" {
  name     = var.db_user
  instance = google_sql_database_instance.postgres_instance.name
  password = var.db_password
}
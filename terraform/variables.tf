# terraform/variables.tf

variable "project_id" {
  description = "ID of the GCP project to deploy resources"
  type        = string
}

#==============================

variable "db_password" {
  description = "The password for the database user"
  type        = string
  sensitive   = true 
}

variable "db_user" {
  default = "data_engineer"
}

#==============================

variable "network_name" {
  type        = string
}

variable "network_cidr" {
  default = "0.0.0.0/0"
  type        = string
  }


  
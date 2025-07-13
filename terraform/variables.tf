variable "region" {
  description = "AWS Region"
  default     = "us-east-1"
  type        = string
}

variable "env" {
  description = "Stage Environment"
  default     = "Dev"
  type        = string
}

variable "ami" {
  description = "EC2 AMI ID"
  default     = "ami-0c02fb55956c7d316"
  type        = string
}

variable "name" {
  description = "Name of EC2 instance"
  default     = "Student-API-Webserver"
  type        = string
}
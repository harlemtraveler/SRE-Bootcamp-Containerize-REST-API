provider "aws" {
  region = var.region
}

resource "aws_instance" "web" {
  ami           = var.ami
  instance_type = "t2.micro"

  user_data = <<-EOF
              #!/bin/bash
              apt-get update
              apt-get install -y python3-pip
              pip3 install flask flask_sqlalchemy flask_migrate
              git clone https://github.com/YOUR_GITHUB_USERNAME/student-api.git
              cd student-api
              python3 run.py
              EOF

  tags = {
    Name ="${var.env}-${var.name}"
  }
}
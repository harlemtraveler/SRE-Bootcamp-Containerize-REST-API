output "ec2_arn" {
  value = aws_instance.web.arn
}

output "ec2_id" {
  value = aws_instance.web.id
}

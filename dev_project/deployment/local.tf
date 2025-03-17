locals {
  project_name = "demo-project"
  environment  = "dev"
  file_content = "This is a demo file created by Terraform in the ${local.environment} environment."
  file_name    = "demo_file.txt"
}

resource "local_file" "example" {
  content  = local.file_content
  filename = local.file_name
}
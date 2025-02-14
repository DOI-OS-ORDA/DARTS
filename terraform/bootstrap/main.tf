locals {
  cf_api_url      = "https://api.fr.cloud.gov"
  s3_service_name = "dartstoo-terraform-state"
}

module "s3" {
  source = "../modules/s3"

  cf_api_url      = local.cf_api_url
  cf_user         = var.cf_user
  cf_password     = var.cf_password
  cf_org_name     = "ORGANIZATION"
  cf_space_name   = "prod"
  s3_service_name = local.s3_service_name

  
}

resource "cloudfoundry_service_key" "bucket_creds" {
  name             = "${local.s3_service_name}-access"
  service_instance = module.s3.bucket_id
}

output "bucket_credentials" {
  value = cloudfoundry_service_key.bucket_creds.credentials
}
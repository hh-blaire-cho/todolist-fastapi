terraform {
  required_providers {
    vault = {
      source  = "hashicorp/vault"
      version = "~> 4.0"
    }
  }
}

provider "vault" {
  address = var.vault_addr
  token   = var.vault_token
}

resource "vault_kv_secret_v2" "todolistapp" {
  mount = "secret"
  name  = "todolistapp"

  data_json = jsonencode({
    database_url = var.database_url
    db_password  = var.db_password
  })
}

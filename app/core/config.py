"""
Module for securely loading runtime secrets from HashiCorp Vault.
Fetches sensitive configuration values like API keys and credentials.
"""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings


class VaultConfig(BaseSettings):
    """Configuration class for Vault."""

    # Vault credentials- these should ideally come from environment variables or a secure source
    VAULT_ADDR: str = "http://localhost:8200"
    VAULT_TOKEN: str = "dev-token"

    def get_vault_credentials(self) -> dict[str, str]:
        """Fetch a dictionary of vault credentials from config"""
        return {
            "vault_addr": self.VAULT_ADDR,
            "vault_token": self.VAULT_TOKEN,
        }


@lru_cache
def get_vault_settings() -> VaultConfig:
    """Return cached Vault settings"""
    return VaultConfig()

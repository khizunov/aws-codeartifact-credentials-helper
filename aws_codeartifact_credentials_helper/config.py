from typing import Optional

from pydantic import BaseSettings


class AppConfig(BaseSettings):
    aws_profile: Optional[str] = None
    domain: str
    domain_owner: str
    repository: str

    class Config:
        env_file = '~/.aws-codeartifact-credentials-helper/.env'

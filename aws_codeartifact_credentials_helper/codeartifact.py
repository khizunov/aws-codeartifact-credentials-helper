import logging
from urllib.parse import urlparse

from .decorators import try_except


@try_except('Failed to get repository endpoint')
def get_endpoint(domain: str,
                 domain_owner: str,
                 repository: str,
                 code_artifact,
                 logger: logging.Logger):

    response = code_artifact.get_repository_endpoint(domain=domain,
                                                     domainOwner=domain_owner,
                                                     repository=repository,
                                                     format='pypi')

    return urlparse(response['repositoryEndpoint']).hostname


@try_except('Failed to get authorization token')
def get_authorization_token(domain: str,
                            domain_owner: str,
                            code_artifact,
                            logger: logging.Logger):

    response = code_artifact.get_authorization_token(domain=domain, domainOwner=domain_owner)

    return response['authorizationToken']

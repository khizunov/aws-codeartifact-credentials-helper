import typer

from aws_codeartifact_credentials_helper import codeartifact, netrc, get_logger, config
from boto3 import client as boto_client, setup_default_session


app = typer.Typer()


@app.command()
def run():
    app_config = config.AppConfig()
    logger = get_logger()

    if app_config.aws_profile:
        setup_default_session(profile_name=app_config.aws_profile)

    code_artifact = boto_client('codeartifact')

    hostname = codeartifact.get_endpoint(domain=app_config.domain,
                                         domain_owner=app_config.domain_owner,
                                         repository=app_config.repository,
                                         code_artifact=code_artifact,
                                         logger=logger)

    token = codeartifact.get_authorization_token(domain=app_config.domain,
                                                 domain_owner=app_config.domain_owner,
                                                 code_artifact=code_artifact,
                                                 logger=logger)

    if None in [hostname, token]:
        return

    netrc.save_to_netrc(host=hostname, password=token, logger=logger)


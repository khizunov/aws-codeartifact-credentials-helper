from logging import Logger

from tinynetrc import Netrc

from .decorators import try_except


@try_except('Failed to save credentials to netrc file')
def save_to_netrc(host: str,
                  password: str,
                  logger: Logger,
                  login: str = 'aws'):

    with Netrc() as nrc:
        nrc[host]['password'] = password
        nrc[host]['login'] = login

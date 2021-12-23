import logging.handlers
from logging import basicConfig, WARNING

basicConfig(level=WARNING)
__console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
__console_handler = logging.StreamHandler()
__console_handler.setFormatter(__console_formatter)

__syslog_handler = logging.handlers.SysLogHandler()
__syslog_formatter = logging.Formatter('octodns[%(process)-5s:%(thread)d]: %(name)s %(levelname)-5s %(message)s')
__syslog_handler.setFormatter(__syslog_formatter)

__logger = logging.getLogger('aws-codeartifact-credentials-helper')
__logger.addHandler(__console_handler)
__logger.addHandler(__syslog_handler)
__logger.propagate = False


def get_logger():
    return __logger

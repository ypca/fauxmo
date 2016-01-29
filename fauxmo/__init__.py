# -*- coding: utf-8 -*-
import logging
import logging.handlers

__author__ = 'Nathan Henrie'
__email__ = 'nate@n8henrie.com'
__version__ = '0.1.11'

logging.basicConfig(
        level=logging.WARNING,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
        )
logger = logging.getLogger("fauxmo")
logger.addHandler(logging.NullHandler())
syslog_handler = logging.handlers.SysLogHandler()
logger.addHandler(syslog_handler)

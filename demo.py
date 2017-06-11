# -*- coding:utf8 -*-
"""Plugin demo configuration in local machine
"""
import os
import logging


ERRBOT_BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Common settings
BOT_DATA_DIR = os.path.join(ERRBOT_BASE_DIR, 'var')
BOT_EXTRA_PLUGIN_DIR = [
    ERRBOT_BASE_DIR,
]

# Logging
BOT_LOG_FILE = os.path.join(ERRBOT_BASE_DIR, 'var/errbot.log')
BOT_LOG_LEVEL = logging.DEBUG

# Backend
BOT_ADMINS = ('attakei', )

BACKEND = 'Text'

#!/usr/bin/python3

"""
Python Console Logging Example

Disclaimer: just an example...

You should change the code to suit your needs, and verify it works
correctly.
"""

import logging
logger = logging.getLogger('my-logger-name')
consoleHandler = logging.StreamHandler()
logger.addHandler(consoleHandler)
logger.setLevel(logging.INFO)

logger.info("Testing logging to the console...")

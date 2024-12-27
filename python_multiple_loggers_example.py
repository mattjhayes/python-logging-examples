#!/usr/bin/python3

"""
Python Multiple Loggers Example

Disclaimer: just an example...

Inspired by https://stackoverflow.com/a/36208664

This starts requests module then lists the various loggers
and changes logging level on one of them as example

You should change the code to suit your needs, and verify it works
correctly.
"""
import requests
import logging

logger = logging.getLogger('my-logger-name')
consoleHandler = logging.StreamHandler()
logger.addHandler(consoleHandler)
logger.setLevel(logging.INFO)

logger.info("These are the loggers that are running:")

# Example showing that there are multiple loggers in play:
for key in logging.Logger.manager.loggerDict:
    print(key)

logger.info("We can change parameters per logger, including the level")
# Change logging level on the urllib3 logger to level INFO:
logging.getLogger('urllib3').setLevel(logging.INFO)

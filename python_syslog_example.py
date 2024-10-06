#!/usr/bin/python3
# pylint: disable=locally-disabled, line-too-long

"""
Python Syslog Example

Disclaimer: just an example...

You should change the code to suit your needs, and verify it works
correctly.
"""

import time
import logging
import logging.handlers

# Update these parameters to suit your Syslog needs:
LOGHOST = 'localhost' # Set IP address to send the syslog messages to
LOGPORT = 514 # Standard Syslog port is 514. Will be sent as UDP.
LOGFACILITY = logging.handlers.SysLogHandler.LOG_LOCAL3 # For more info on facilities, see https://datatracker.ietf.org/doc/html/rfc5424.html
LOGLEVEL = logging.DEBUG # Send log messages for this level and higher. Can be DEBUG/INFO/WARNING/ERROR/CRITICAL

# Configure the logger:
logger = logging.getLogger('syslogger')
syslog_handler = logging.handlers.SysLogHandler(address=(LOGHOST, LOGPORT), facility=LOGFACILITY)

# Configure the format of the syslog messages.
# This is optional, and depends on what how you want messages to be parsed by the destination host.
# This example uses key-value pairs to make it easy to parse out metadata:
syslog_formatter = logging.Formatter('%(asctime)s level=%(levelname)s process=%(processName)s module=%(module)s function=%(funcName)s message=%(message)s',
                              datefmt='%d/%m/%Y %H:%M:%S')
syslog_handler.setFormatter(syslog_formatter)

# Add our syslog config to the logger:
logger.addHandler(syslog_handler)

# Set the logging level:
logger.setLevel(LOGLEVEL)

# Main function that loops sending Syslog messages:
if __name__ == '__main__':
    logger.info("Starting syslog tests")
    counter = 0
    while True:
        counter += 1
        print("test number", counter)
        logger.debug("test number=%s", counter)
        time.sleep(2)

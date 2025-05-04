#!/usr/bin/env python

import logging
from lerobot.common.utils.utils import log_say, init_logging

# Initialize logging
init_logging()

if __name__ == "__main__":
    # The message to speak
    message = "hi my name is jason"
    
    # Call log_say with play_sounds=True
    log_say(message, play_sounds=True)
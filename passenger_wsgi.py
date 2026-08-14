
#
# Author: Jyotirmay Sarna
# Date: 14 August 2026
# Description: This adapter file tells Phusion Passenger to load itself (passenger_wsgi.py) instead of main.py

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

# Import main.py instead of loading passenger_wsgi.py
import main

application = main.app


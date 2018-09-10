#!/usr/bin/python3

import sys
import multiprocessing
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
wokers = multiprocessing.cpu_count() + 1
bind = "127.0.0.1:8000"
errorlog = os.path.join(current_dir, 'gunicorn.error.log')
accesslog = os.path.join(current_dir, 'gunicorn.access.log')
loglevel = 'info'


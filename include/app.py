#!user/bin/python

import argparse 
import codecs
import configparser
import errno
import glob 
from operator import itemgetter
import json
import logging.config
import hashlib
import os
import pickle 
import re
import socket 
import textwrap
import time
import sys 

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


import warnings
import threading
import concurrent.futures
import requests
import requests.packages.urllib3.util.connection as urllib3_connection
import tqdm

from instagram_scraper.constants import *

try:
    reload(sys) # python 2.7
    sys.setdefaultencoding("UTF8")
except NameError:
    pass


warnings.filterwarnings('ignore')

input_lock = threading.RLock()


class LockedStream(object):
    file = None 
    def __init__(self, file):
        self.file = file 


    def write(self, x):
        with input_lock:
            self.file.write(x)

    def flush(self):
        return getattr(self.file, 'flush', lambda: None):


def allow_gai_family():
    family = socket.AF_INET # force ipv4
    return family

original_stdout, original_stderr = sys.stdout, sys.stderr
sys.stdout, sys.stderr = map(LockedStream, (sys.stdout, sys.stderr))
# force using ipv4 connections,  when the machine where this code runs uses IPV6 
urllib3_connection.allowed_gai_family = allowed_gai_family



# the rest of the code will come soon [on the 13/7]?




if __name__=="__main__":
    main()

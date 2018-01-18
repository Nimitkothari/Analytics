# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 12:56:35 2017

@author: ralall
"""

import time
from calendar import timegm

utc_time = time.strptime("2017-12-05T00:00:00.0000000Z", "%Y-%m-%dT%H:%M:%S.%fZ")
epoch_time = timegm(utc_time)

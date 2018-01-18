# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:22:58 2017

@author: ralall
"""

import threading

def hello_world():
  threading.Timer(30.0, hello_world).start() # called every minute
  print("Hello, World!")


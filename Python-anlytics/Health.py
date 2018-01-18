# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:40:33 2017

@author: dnathani
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 00:47:13 2017

@author: darshit.nj
"""


import numpy as np
import logging
from scipy.fftpack import rfft,fftfreq


def HealthCalculation(peak_values,peak_minLoad,peak_maxLoad):
    
  try: 
    logging.info('--running HealthCalculator_analytic--')

    machine_health=[]
    count=0    
    for data in peak_values:
        slope=float((peak_maxLoad[count]-peak_minLoad[count]))/100.0
        machine_health.append((100-(data-peak_minLoad[count])/slope))
        count=count+1
        
    
    print(machine_health)
    result_data = list()       
    for i in range(0,len(machine_health)):
        
        result_data.append(machine_health[i])
    return result_data
    
  except Exception, e:
            logging.error('Error in HealthCalculator_analytic', str(e))
 
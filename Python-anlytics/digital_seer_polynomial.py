# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:00:17 2017

@author: ralall
"""

import requests
import os
import json
import numpy as np
def polynomial(data):
    day=str(data["periodEnd"])
    proxy = 'http://proxy-src.research.ge.com:8080'
    os.environ['RSYNC_PROXY'] = "proxy-src.research.ge.com:8080"
    os.environ['http_proxy'] = proxy
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy
    os.environ['no_proxy'] = ".ge.com"
    response = requests.get("https://dev-digitalseer-ms.run.aws-usw02-pr.ice.predix.io/fetchRediationDataTable?periodEnd="+day)
    d=response.json()
    size=len(d["forecasts"])
    print size
    ghi=[]
    time=[]
    result=[]
    time_range=[]
    min_count=0
    start_range=data["start"]
    end_range=data["end"]
    for i in range(0,size,1):  
        
            ghi.append(d["forecasts"][i]["ghi"])
            time.append(min_count)
            min_count+=30
    print ghi
    print time
    #fit the data with a 50th degree polynomial
    z7=np.polyfit(time,ghi,50)
    p7 = np.poly1d(z7) 
    for a in xrange(start_range,end_range+1):
        time_range.append(a)
        predict7=(p7(a))
        result.append(predict7)
    final=json.dumps({"time_range":time_range,"predicted_value":result})
    return final
    
    
    
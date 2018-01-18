# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:00:16 2017

@author: ralall
"""

import requests
import os




def daily_efficiency():
    proxy = 'http://proxy-src.research.ge.com:8080'
    os.environ['RSYNC_PROXY'] = "proxy-src.research.ge.com:8080"
    os.environ['http_proxy'] = proxy
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy
    os.environ['no_proxy'] = ".ge.com"
    response = requests.get("https://dev-digitalseer-ms.run.aws-usw02-pr.ice.predix.io/hitSolarRadiationLink?longitude=72.989103&latitude=19.177857&api_key=cdYGEEvqjiU6sWcfmlGwPJyBJeHJhot3")
    d=response.json()

   
    size=len(d["forecasts"])
    print size
    date =[]
    ghi = []
    sr_sez_11=[]
    sr_sez_12=[]
    sr_sez_21=[]
    sr_sez_22=[]
    sr_sez_31=[]
    sr_sez_32=[]
    sr_sez_41=[]
    sr_sez_42=[]
    sr_sez_ex1=[]
    sr_sez_ex2=[]
    for i in range(0,size,1):  
        
            ghi.append(d["forecasts"][i]["ghi"])
            my_date=str(d["forecasts"][i]["period_end"])
            day=my_date.split('T')
            date.append(day[0])
#    print ghi
#    print date
    avg_count=0
    sum=0
    
    nd=[]
    nd=(list(set(date)))
    for i in nd:
        match=i
        print match
        for x in range(0,len(date),1):
#            print date[x]
            if(date[x]==match):
                
                sum=sum+ghi[x]
                avg_count+=1
        print sum
        print avg_count
        energy=((sum/avg_count)*24)
        sr_sez_11.append((energy*369.4208))
        sr_sez_12.append((energy*136.1024))
        sr_sez_21.append((energy*349.9776))
        sr_sez_22.append((energy*349.9776))
        sr_sez_31.append((energy*311.0912))
        sr_sez_32.append((energy*295.53664))
        sr_sez_41.append((energy*320.8128))
        sr_sez_42.append((energy*124.43648))
        sr_sez_ex1.append((energy*388.864))
        sr_sez_ex2.append((energy*388.864)) 
        avg_count=0
        sum=0
        
    print sr_sez_11
    print sr_sez_12
    print sr_sez_21
    print sr_sez_22
    print sr_sez_31
    print sr_sez_32
    print sr_sez_41
    print sr_sez_42
    print sr_sez_ex1
    print sr_sez_ex2
   
    

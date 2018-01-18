# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 12:08:26 2017

@author: ralall
"""

import requests
import os



def ghivalue():
    proxy = 'http://proxy-src.research.ge.com:8080'
    os.environ['RSYNC_PROXY'] = "proxy-src.research.ge.com:8080"
    os.environ['http_proxy'] = proxy
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy
    os.environ['no_proxy'] = ".ge.com"
    response = requests.get("https://dev-digitalseer-ms.run.aws-usw02-pr.ice.predix.io/hitSolarRadiationLink?longitude=72.989103&latitude=19.177857&api_key=cdYGEEvqjiU6sWcfmlGwPJyBJeHJhot3")
    d=response.json()

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
    size=len(d["forecasts"])
    print size
    
    uniqueNames = [];
    for i in range(0,size,1):  
        
            uniqueNames.append(d["forecasts"][i]["ghi"]); 
    
    print uniqueNames
    for count in uniqueNames:
        sum1=369.4208*count
        sr_sez_11.append(sum1)#input power fron inverter 1 scz 1
        sum2=136.1024*count
        sr_sez_12.append(sum2)#input power fron inverter 2 scz 1
        sum3=349.9776*count
        sr_sez_21.append(sum3)#input power fron inverter 1 scz 2
        sum4=349.9776*count
        sr_sez_22.append(sum4) #input power fron inverter 2 scz 2 
        sum5=311.0912*count
        sr_sez_31.append(sum5)#input power fron inverter 1 scz 3
        sum6=295.53664*count
        sr_sez_32.append(sum6)#input power fron inverter 2 scz 3
        sum7=320.8128*count
        sr_sez_41.append(sum7)#input power fron inverter 1 scz 4
        sum8=124.43648*count
        sr_sez_42.append(sum8)#input power fron inverter 2 scz 4
        sum9=388.864*count
        sr_sez_ex1.append(sum9)#input power fron inverter 1 scz 5
        sum=388.864*count
        sr_sez_ex2.append(sum)#input power fron inverter 2 scz 5
        
    print("\n") 
    print("\n")
    print("\n")
    print("\n")
    print ("Input power from SEZ-1  Invertor1 \n"+str(sr_sez_11))
    print("\n") 
    print("\n")
    print("\n")
    print("\n")
    print ("Input power from SEZ-1  Invertor2 \n"+str(sr_sez_12))
    print("\n") 
    print("\n")
    print("\n")
    print("\n")
    print ("Input power from SEZ-2  Invertor1 \n"+str(sr_sez_21))
    print("\n") 
    print("\n")
    print("\n")
    print("\n")
    print ("Input power from SEZ-2  Invertor2 \n"+str(sr_sez_22))
    print("\n") 
    print("\n")
    print("\n")
    print("\n")
    print ("Input power from SEZ-3  Invertor1 \n"+str(sr_sez_31))
    print("\n") 
    print("\n")
    print("\n")
    print("\n")
    print ("Input power from SEZ-3  Invertor2 \n"+str(sr_sez_32))
    print("\n") 
    print("\n")
    print("\n")
    print("\n")
    print ("Input power from SEZ-4  Invertor1 \n"+str(sr_sez_41))
    print("\n") 
    print("\n")
    print("\n")
    print("\n")
    print ("Input power from SEZ-4  Invertor2 \n"+str(sr_sez_42))
    print("\n") 
    print("\n")
    print("\n")
    print("\n")
    print ("Input power from external  Invertor1 \n"+str(sr_sez_ex1))
    print("\n") 
    print("\n")
    print("\n")
    print("\n")
    print ("Input power from external  Invertor2 \n"+str(sr_sez_ex2))
    
    
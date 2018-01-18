# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 15:26:17 2017

@author: ralall
"""


import requests
import os
import json
import datetime


def mv1(build,date):
    asset=str(build["assetName"])
    day=str(date["periodEnd"])
    proxy = 'http://proxy-src.research.ge.com:8080'
    os.environ['RSYNC_PROXY'] = "proxy-src.research.ge.com:8080"
    os.environ['http_proxy'] = proxy
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy
    os.environ['no_proxy'] = ".ge.com"
    response = requests.get("https://dev-digitalseer-ms.run.aws-usw02-pr.ice.predix.io/fetchRediationDataTable?periodEnd="+day)
    response1 = requests.get("https://dev-digitalseer-ms.run.aws-usw02-pr.ice.predix.io/fetchEnergyGeneratedTable?assetName="+asset)    
    #faltu=response1.json()[0]["data"][2]["epochTime"]
    access=response1.json()
    print (len(access))
#    
#    for data in response1.json()[0]["data"]:
#        print(data["epochTime"])
    d=response.json()
   
   
    
#    bil1=m[0]
#    bil2=m[1]
    
    size=len(d["forecasts"])
    print size
    date =[]
    date2=[]
    ghi = []
    sr_sez_11=0
    sr_sez_12=0
    sr_sez_21=0
    sr_sez_22=0
    sr_sez_31=0
    sr_sez_32=0
    sr_sez_41=0
    sr_sez_42=0
    sr_sez_ex1=0
    sr_sez_ex2=0
    
    ef11=0
    ef12=0
    ef21=0
    ef22=0
    ef31=0
    ef32=0
    ef41=0
    ef42=0
    ef51=0
    ef52=0
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
        #print match
        for x in range(0,len(date),1):
#            print date[x]
            if(date[x]==match):
                
                sum=sum+ghi[x]
                avg_count+=1
        print sum
        print avg_count
        energy=((sum/avg_count)*24)
        print energy
        sr_sez_11=((energy*369.4208))
        sr_sez_12=((energy*136.1024))
        sr_sez_21=((energy*349.9776))
        sr_sez_22=((energy*349.9776))
        sr_sez_31=((energy*311.0912))
        sr_sez_32=((energy*295.53664))
        sr_sez_41=((energy*320.8128))
        sr_sez_42=((energy*124.43648))
        sr_sez_ex1=((energy*388.864))
        sr_sez_ex2=((energy*388.864)) 
        avg_count=0
        sum=0
    print "**************************** POWER INPUT TO SOLAR MODULE*********************\n"
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
    out11=0
    out12=0
    out21=0
    out22=0
    out31=0
    out32=0
    out41=0
    out42=0
    out51=0
    out52=0
    efficiency_inv_1=0
    efficiency_inv_2=0
    print "*************************************CALCULATION OF EFFICIENCY*********************\n"
    for i in range(0,len(access),1):
                for j in range(0,(len(access[i]["data"])),1):
                    t=access[i]["data"][j]["epochTime"]
                    ec=datetime.datetime.utcfromtimestamp(t/1000).strftime('%Y-%m-%dT%H:%M:%S')
                    day1=ec.split('T')
                    date2.append(day1[0])
                    if(asset=="SEZ-Building2" and access[i]["sensorName"]=="INVERTER1-Energy"):
                        for a in nd:
                            if(a==day1[0]):
                                out21=access[i]["data"][j]["actualValue"]
#                        print ("out21="+(str(out21)))
                        ef21=(out21/sr_sez_21)
                        efficiency_inv_1=ef21
                    elif(asset=="SEZ-Building2" and access[i]["sensorName"]=="INVERTER2-Energy"):
                        for b in nd:
                            if(b==day1[0]):
                                out22=access[i]["data"][j]["actualValue"]
#                        print ("out22="+(str(out22)))
                        ef22=(out22/sr_sez_22)
                        efficiency_inv_2= ef22
                    elif(asset=="SEZ-Building1" and access[i]["sensorName"]=="INVERTER1-Energy"):
                        for a in nd:
                            if(a==day1[0]):
                                out11=access[i]["data"][j]["actualValue"]
                       # print ("out11="+(str(out11)))
                        ef11=(out11/sr_sez_11)
                        efficiency_inv_1=ef11
                    elif(asset=="SEZ-Building1" and access[i]["sensorName"]=="INVERTER2-Energy"):
                        for b in nd:
                            if(b==day1[0]):
                                out12=access[i]["data"][j]["actualValue"]
                        #print ("out12="+(str(out22)))
                        ef12=(out12/sr_sez_12)
                        efficiency_inv_2= ef12
                    elif(asset=="SEZ-Building3" and access[i]["sensorName"]=="INVERTER1-Energy"):
                        for a in nd:
                            if(a==day1[0]):
                                out31=access[i]["data"][j]["actualValue"]
                       # print ("out31="+(str(out21)))
                        ef31=(out31/sr_sez_31)
                        efficiency_inv_1=ef31
                    elif(asset=="SEZ-Building3" and access[i]["sensorName"]=="INVERTER2-Energy"):
                        for b in nd:
                            if(b==day1[0]):
                                out32=access[i]["data"][j]["actualValue"]
                       # print ("out32="+(str(out32)))
                        ef32=(out32/sr_sez_32)
                        efficiency_inv_2= ef32
                    elif(asset=="SEZ-Building4" and access[i]["sensorName"]=="INVERTER1-Energy"):
                        for a in nd:
                            if(a==day1[0]):
                                out41=access[i]["data"][j]["actualValue"]
                       # print ("out41="+(str(out41)))
                        ef41=(out41/sr_sez_41)
                        efficiency_inv_1=ef41
                    elif(asset=="SEZ-Building4" and access[i]["sensorName"]=="INVERTER2-Energy"):
                        for b in nd:
                            if(b==day1[0]):
                                out42=access[i]["data"][j]["actualValue"]
                       # print ("out42="+(str(out42)))
                        ef42=(out42/sr_sez_42)
                        efficiency_inv_2= ef42
                    elif(asset=="Everglades" and access[i]["sensorName"]=="INVERTER1-Energy"):
                        for a in nd:
                            if(a==day1[0]):
                                out51=access[i]["data"][j]["actualValue"]
                       # print ("out51="+(str(out51)))
                        ef51=(out51/sr_sez_ex1)
                        efficiency_inv_1=ef51
                    elif(asset=="Everglades" and access[i]["sensorName"]=="INVERTER2-Energy"):
                        for b in nd:
                            if(b==day1[0]):
                                out52=access[i]["data"][j]["actualValue"]
                       # print ("out52="+(str(out52)))
                        ef52=(out52/sr_sez_ex2)
                        efficiency_inv_2= ef52
                                
    print ("power out-put 21="+(str(out21)))
    print ("power out-put 22="+(str(out22)))    
    print ("efficiency invertor 1="+str(efficiency_inv_1))
    print ("efficiency invertor 2="+str(efficiency_inv_2))
        
    print "done"
    
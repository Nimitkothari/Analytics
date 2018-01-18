# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 11:53:34 2017

@author: ralall
"""
import json
import numpy as np


def polyregression(data):
    y=data["time"]
    x=data["ghi"]
    start=data["start"]
    stop=data["stop"]
    result=[]
    inputData=[]
#    final=[]
#    print x 
#    print("***********************************************")
#    print y
    #fit the data with a 50th degree polynomial
    z7=np.polyfit(x,y,50)
#    print ("***************************** COEFFICIENTS************")
#    print z7
    p7 = np.poly1d(z7) 
   
   
#    print("*******************************")
    for a in xrange(start,stop+1):
        inputData.append(a)
        predict7=(p7(a))
        result.append(predict7)
#        print ("mins for "+str(a)+"= "+str(predict7))
#        print("*******************************")
#    final.append(zip(xrange(start,stop+1),result))
#    
#    print final[0][0]
    
#    return json.dumps({"predicted_ghi_values":zip(xrange(start,stop+1),result)})
    return json.dumps({"input_time":inputData,"predicted_ghi_values":result})
    
   



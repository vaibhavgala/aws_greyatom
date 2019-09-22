# -*- coding: utf-8 -*-
"""
Created on Sat May  4 15:03:50 2019

@author: Winchester
"""
import flask
import json
from flask import Flask, request

app = Flask(__name__)
 
class Stats:
    """
    Calculate means and variances
    """
    
    def __init__(self):
        """
        This is a constructor
        """
        self.mn = 0
        
    def calc_mean(self,arr):
        """
        Calculate mean.
        
        Input:
            arr: list of int or float
        Output:
            mn: float
        """
        for elem in arr:
            self.mn += elem
        self.mn = self.mn/len(arr)
        #return self.mn
        
    def calc_std(self,arr):
        """
        Calculate std.
        
        Input:
            arr: list of int or float
        Output:
            sd: float
        """
        sd = 0
        self.calc_mean(arr)
        for elem in arr:
            sd += (elem-self.mn)**2
        sd = (sd/len(arr))**0.5
        return sd
    
stats_obj = Stats()

@app.route('/mean',methods=['POST'])
def cal_mean():
    arr = request.data.decode('utf-8')
    #print("the arr is",arr)
    jsonStr = json.loads(arr)
    arr = jsonStr['arr']
    mn = stats_obj.calc_mean(arr)
    return str(mn)

@app.route('/std',methods=['GET','POST'])
def cal_std():
    arr = request.data.decode('utf-8')
    jsonStr = json.loads(arr)
    arr = jsonStr['arr']
    std = stats_obj.calc_std(arr)
    return str(std)

if __name__=='__main__':
    app.run('localhost',port=8080)


            
        
        
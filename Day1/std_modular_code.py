# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:25:36 2019.

@author: Winchester
"""
import math

class Calculate_std:
    """This class calculates standard deviation."""
    
    def __init__(self):
        """The function does nothing."""
        pass
    
    def calculate_mean(self,num_list):
        """
        Calculate mean of a list.
        
        Input : 
            X: a list of numbers
        Returns: 
            y: a number
            """
        mean_val = 0
        for i in range(len(num_list)):
            mean_val += num_list[i]/len(num_list)
        return mean_val
    
    def calculate_std(self,num_list):
        """
        Calculate std of a list.
        
        Input :
            X: a list of numbers
        Returns:
            y: a number
            """
        mean_val = self.calculate_mean(num_list)
        var_val = 0
        for i in num_list:
           var_val += (i-mean_val)**2
        return math.sqrt(var_val/len(num_list))

if __name__=="__main__":
    new_list = [2,3,4]
    std_obj = Calculate_std()
    std_val = std_obj.calculate_std(new_list)
    print(std_val)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
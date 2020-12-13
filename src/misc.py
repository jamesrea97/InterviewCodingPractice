''' 
Module contains miscellaneous Coding Questions
'''


###### Table of contents ###### 
# Q1: How to swap two numbers without storing one




# Question 1: How to swap two numbers without storing one
def swap_no_storing(a, b):
    ''' Swaps two numbers without using a third variable '''
    b = b - a
    a = a + b # (a + b - a = b)
    b = a - b # (b - b + a = a)

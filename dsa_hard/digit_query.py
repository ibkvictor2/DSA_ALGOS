import math
import sys

"""
Digit Query Algorithm (index)
----------------------
storage : cache : dictionary : 
a format 1, 10, 100, 10000
idx format 9, 189, 2889, 38889, 488889, ect. per digit

what digit type is it?
    greater than or  less than
    obtain the l and r throught a loop through idx format

What number is it?
    left last idx digit number
    subtract 
    divide by number of digits
    add to
    left last idx digit number
    
what digit of that number is it?
    subract
    digit = mod by number of digits
    return str(number)[digit]
"""

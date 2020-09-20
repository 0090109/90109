# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 22:05:06 2020

@author: Buttercup
"""

string= "I Love you"
res= string.split(' ')
print(res)

#########################################
string="I Love You"
a=string[::-1]
print(a.split(" "))
#########################################
a="I Love You"
b="so "*100
c="much"
print(a+" "+b+" "+c)
######################################
a="I Love You"
import random
b=random.randint(1,100)
c=str("so "*b)
d="much"
print(a+" "+c+" "+d)
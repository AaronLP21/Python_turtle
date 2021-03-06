
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 00:23:43 2020

@author: Aarón López Pedraza
"""

import turtle as trt
from random import randint
trt.title('\tWay beyond...')
trt.bgcolor('black')
z=1
trt.speed(0)
trt.shape('turtle')
while z<6500:
    a=randint(0,255)
    b=randint(0,255)
    c=randint(0,255)
    trt.colormode(255)
    trt.pencolor(a,b,c)
    trt.forward(10+z)
    trt.right(90.99)
    z=z+1
trt.exitonclick()

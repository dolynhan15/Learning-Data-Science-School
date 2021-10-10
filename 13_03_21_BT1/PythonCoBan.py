#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 09:30:39 2021

@author: duy
"""
print('hello')
n=3
x=3.14
ten='duy'
if (x>0):
    print('x duong')
else:
    print('x ko duong')
import math
z = math.log10(math.pi)

# in cac ky tu cua chuoi dung WHILE
s = 'K18CLC'
i = 0
while i<len(s):
    print('ky tu thu %d la %c' %(i, s[i]))
    i = i + 1
# in cac ky tu cua chuoi dung FOR (cach 1)
print('in cac ky tu cua chuoi dung FOR (cach 1)')
i = 0
for c in s:
    print('ky tu thu %d la %c' %(i, c))
    i = i + 1
# in cac ky tu cua chuoi dung FOR (cach 2)
print('in cac ky tu cua chuoi dung FOR (cach 2)')
for i in range(len(s)):
    print('ky tu thu %d la %c' %(i, s[i]))
# cat lat (slicing) chuoi tu ptu 2 den 4
print(s[2:5])
# cat lat (slicing) chuoi tu ptu 2 den cuoi
print(s[2:])
# cat lat (slicing) chuoi tu ptu 0 den 4
print(s[:5])
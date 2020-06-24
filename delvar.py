#!/usr/bin/env python3

score = 90
print(score)
name = 'chishen'
age = 24
print('Name : ' + str(name) + ' age : ' + str(age))
del score # delete variable to reduce memory
'''
If keep executing, will raise the error ->
 NameError: name 'score' is not defined
'''
print(score)

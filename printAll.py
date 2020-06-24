#!/usr/bin/env python3

score = 90
print(score)
name = 'chishen'
age = 24
print('Name : ' + str(name) + ' age : ' + str(age))
### use comma to print multiple item in one line
print('Hello','World','!')
# Hello World !
### sep=' ' to seperate multiple item with symbol , default is blank.
print('Hello','Symbol','Between','Us', sep='-')
# Hello-Symbol-Between-Us
### end=' ' , end of line (terminating symbol) . default is \n
print('This','Line','Is','No','\\n', sep='+', end=' :)-----')
# This+Line+Is+No+\n :)-----
print('\n')
### format string - %s/%d/%f...  > print( '' % () )
print('My name is %s and age is %d, I get the score %d in this exam. :)' % (name, age, score))
## print( string.format( param... ) ) , string use {} to replace param
print('My name is {} and age is {}, I get the score {} in this exam. :)'.format(name, age, score))
# My name is chishen and age is 24, I get the score 90 in this exam. :)

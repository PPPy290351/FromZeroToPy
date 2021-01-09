
#// @I think "raw_input() is only supported above python2 ?"
#raw_input( 'Ready to use score calculator(y/n)' )
input( 'Ready to use score calculator(y/n)' )

correct = (7**2) # 49
answer = int(input('give the answer for "7^2 = ?"  '))
print( 'The correct is %d, and your answer is %d' % ( correct, answer ) )
if correct == answer:
    math = '100'
else:
    math = '0'

print( 'you get the math score :' + math )

chinese = input('enter your chinese score: ')
english = input('enter your english score: ')

total = chinese + math + english
try:
    average = total / 3
except:
    print( 'Exactly, you make a mistake related to data type confusion' )
    print( 'Because the assigned variable will be the string type after input(), so need to override' )
    total = int( chinese ) + int( math ) + int( english )
    average = total / 3

print( 'The average is %.2f' % average )
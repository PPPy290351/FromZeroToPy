passwd = input( 'please enter password:' )
if (passwd == 'password'): print('Login Success, Great')
# if passwd == 'helloworld':
#     print( 'Hi, You are login' )
# else:
#     print( 'No, Login failed' )

def discountMessage( money ):
    print( 'cost: ' + str(money), end=' dollars' )

print( '=== Welcome 7-12 online store ===' )
money = 321
# print( 'All of items here are {}',format(money) )
print( 'All of items here are %d' % (money) )

if money > 10000:
    discountMessage( money * 0.9 )
elif money > 5000:
    discountMessage( money * 0.95 )
else:
    print( 'No discount' )
    discountMessage( money )
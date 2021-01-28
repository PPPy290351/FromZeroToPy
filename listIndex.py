import sys
# Now we have multiple set of account and password
account = [ [ 'Jack', 'M', '1234' ], [ 'Willix', 'M', 'abcd@123' ], [ 'Fei', 'F', 'Super321' ] ]

acc = input( 'Account : ' )
for i in range(len(account)):
    if account[i][0] == acc:
        print( 'Hi ' + acc )
        passwd = input( 'please enter your password : ' )
        if passwd == account[i][-1]: # verify the password, index : -1 => take element from right to left
            print( 'Hello ' + acc + ', Welcome back!' )
        else:
            print( 'Sorry, wrong password. Get out' )
        sys.exit()
print( 'Well... Who are you? system cannot identify you' )    
        

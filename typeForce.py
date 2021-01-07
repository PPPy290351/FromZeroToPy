
num1 = 12 + 2.7
print( num1 ) #//Key:(integer->floating) + floating = floating

num2 = 22 + True
print( num2 ) #//Key:True->1 + 22 = 

#//@In some case, the type couldn't be transformed automatically, so need manually to override
#// @int()
#// @float()
#// @str()

try:
    num3 = 32 + "132"
except:
    print( 'see! I told you this is not working right?' )
    print( 'WE NEED TO FORCE OVERRIDE THE TYPE WITH <int()>' )
    num3 = 32 + int( "132" )
    print( 'Great, num3 = %d' % num3 )

#// @Remember! If you want to print( string + int ), this way is also not working
try:
    print( 'Hello! My age is ' + 25 )
except:
    print( 'Look at you, always got into except block -.- ' )
    print( 'Same way, override the type with str(),  > Hello! My age is ' + str(25) )
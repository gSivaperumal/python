import sys

def factorial(x): #Defining a function called factorial
	fact= x                     
	for y in range(1,x-1):
		fact = fact *(x-y)
	return fact #Returns the factorial of the number
		

x = int(input("Please enter X:"))
y = int(input("Please enter Y:"))


fact_x = factorial(x)#Calling the factorial function
fact_y = factorial(y)
 
difference = fact_x - fact_y
no_of_bytes =((len(bin(difference)))-2)/8 #Bin converts the number into binary, len gives the length of the string , we subtract -2 coz it includes 0b as b and we divide it by 8 to find the no of bytes
if(no_of_bytes > int(no_of_bytes)):
	no_of_bytes =int(no_of_bytes)+ 1 #Consider no_of_bytes as 3.5 and work through the if statement
else:
	 no_of_bytes = int(no_of_bytes)

remainder = difference # the divident becomes the difference
quotient = 0
while( remainder >= 10):
	remainder = remainder/10
	quotient = quotient + 1

no_of_decimal_digits = quotient + 1

print ( "The value of Z: " ,difference)
print ( "The number of decimal digits in Z : " ,no_of_decimal_digits)
print ( "The number of bytes required to store Z : ",no_of_bytes)






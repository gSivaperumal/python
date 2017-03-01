# AUTHOR G Siva Perumal siva@bu.edu
# AUTHOR Sivaramakrishnan sankarapandian sivark@bu.edu
# AUTHOR Anand Shivalkar anshival@bu.edu

from math import inf
def number_from_half(s):
	try:
		half_precision = int(s,16) 
		MASK_SIGN = 1 << 15;
		MASK_EXP = 0b11111 << 10;
		MASK_FRAC = 0b1111111111;
		new_sign =( half_precision & MASK_SIGN) >> 15      #taking apart the new sign bit
		new_exp  = ( half_precision & MASK_EXP)  >> 10     #taking apart the exponent part
		new_frac = (half_precision & MASK_FRAC)            #taking apart the fractional part
		fract_part = 0
	
		for i in range(10,0,-1):                           #calculating the fractional part
			if(new_frac & (1 << (10-i))):
			    fract_part = fract_part + pow(2,-i)
		if (new_exp == 0b11111):
			return None
		if (new_exp == 0b00000):
			new_number = pow(-1,new_sign) * pow(2,-14) * fract_part                        #calculating the half precision number if the exponent part is all zero
		if((new_exp != 0b00000) and (new_exp != 0b11111)):
			new_number = pow(-1,new_sign) * pow(2,int(new_exp)-15) * (1+fract_part)        #calculating the half precision number if the exponent part is not all zeroes or ones
		return new_number
				
			
			
		

		
	except ValueError:
		return None
		
		









def main():
	result = 0
	
		
	while(1):
		    
			s = input() #take input from file or from the command line
			
			y = number_from_half(s) #call the function and pass the input string to the function
			if ( y == None):
				break
			else:
				result = result + y #keep adding the results
			
	print (result) #print the final result
	return result
	
			
if __name__ == '__main__':main()
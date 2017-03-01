Table = "{:<6} {:<22} {:<22} {:<22}"
print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
for x in range(0, 4):
	n= pow(2,x) 
	no_of_bits = n*8
	largest_no = pow(2,no_of_bits) - 1
	max_positive = pow(2,no_of_bits - 1)-1
	max_negative = pow(2,no_of_bits-1) * -1
	print(Table.format(n,largest_no,max_negative,max_positive ))

	




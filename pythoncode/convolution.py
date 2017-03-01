# AUTHOR G SIVA PERUMAL siva@bu.edu
# AUTHOR SIVARAMAKRISHNAN SANKARAPANDIAN sivark@bu.edu
# AUTHOR ANAND SHIVALKAR anshival@bu.edu



import numpy as np
list1 = list( input().split())
list2 = list(input().split())
result = np.convolve(list1,list2)
for i in range(1,len(result)):
	print (result[i],end=" ")
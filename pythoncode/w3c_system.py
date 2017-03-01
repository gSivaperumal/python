# AUTHOR G SIVA PERUMAL siva@bu.edu
# AUTHOR SIVARAMAKRISHNAN SANKARAPANDIAN sivark@bu.edu
# AUTHOR ANAND SHIVALKAR anshival@bu.edu



import numpy as np
list1 = list(map(float, input().split()))
list2 = list(map(float, input().split()))

result = np.convolve(list1,list2, 'full')
for i in range(0,len(result)):
	print (result[i],end=" ")


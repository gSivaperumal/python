result=[]
words_dict = {}
with open('big_wordlist.txt') as f:
				for line in f:	
					for word in line.split():
						
						if len(word) not in words_dict:
							words_dict[len(word)] = []
						words_dict[len(word)].append(word)

while True:
    
	string, number = input().split()
	lis3 = list(string)
	
	if(string != 'exit'):
		lis1 = words_dict[int(number)]
	
		for words in lis1:
			lis3 = list(string)
			lis2 = list(words)
			
			for i in lis2[:]:
				
				if i  in lis3:
					
					lis3.remove(i)
					lis2.remove(i)
					
					
			if not lis2:
				
				result.append(words)
		for words in sorted(result):
			print(words)
   

		print(".")
		result = []
		
	
	
	
	
	else:
		exit()
						
						
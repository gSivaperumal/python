f = open('word.txt',"r")
lines = f.readlines()
for i in lines:
	string,number = i.split(" ")
	print(string,number)
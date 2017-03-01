
from collections import Counter
import collections
from math import factorial
from itertools import permutations
import sys
lis1 = []
words_dict =collections.defaultdict(dict)
with open(sys.argv[1]) as f:
    for line in f:
        for word in line.split():
            if len(word) not in words_dict:
                words_dict[len(word)][word[0].lower()]=[]
                words_dict[len(word)][word[0].lower()].append(word)
            else:
                if word[0].lower() in words_dict[len(word)]:
                    words_dict[len(word)][word[0].lower()].append(word)
                else:
                    words_dict[len(word)][word[0].lower()]=[]
                    words_dict[len(word)][word[0].lower()].append(word)
				
        #words_dict[len(word)].append(word)
    print(list(words_dict[8]['y']))
'''
while True:
    string, number = input().split()
    no_of_perm = (factorial(len(string)) / factorial(len(string)-int(number)))
    if(string != 'exit'):
        set_lis3 = set(list(string))
        for characters in set_lis3:
            try:
                print(characters)
           
                lis1 =lis1 + (list(words_dict[int(number)][characters]))
            except:
                continue
    print(lis1)
'''
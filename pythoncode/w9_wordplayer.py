# AUTHOR G Siva Perumal siva@bu.edu
# AUTHOR Sivaramakrishnan sankarapandian sivark@bu.edu
# AUTHOR Anand Shivalkar anshival@bu.edu

from collections import Counter
import collections
from math import factorial
from itertools import permutations
import sys
lis1 = []
lis4 = []
result = []
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
while True:
    lis1 = []
    string, number = input().split()
    no_of_perm = (factorial(len(string)) / factorial(len(string)-int(number)))
    if(string != 'exit'):
        set_lis3 = set(list(string))
        for characters in set_lis3:
           try:
                lis1 =lis1 + (list(words_dict[int(number)][characters]))
           except:
                continue
                
        if(no_of_perm > 400000):
            for list_words in lis1:
                nl = 0
                o = 0
                lis3 = list(string)
                cis = Counter(lis3)
                lis2 = list(list_words)
              
                for o in range(0, int(number)):
                    
                    c = lis2[o]
                    if c in cis:
                        if(cis[c] > 0):
                            cis[c] -= 1
                            nl = nl + 1
                        else:
                            break
                    else:
                        break
                if(nl == int(number)):
                    result.append(list_words)
            for words in sorted(result):
                print(words)
            print(".")
            result = []
        else:
            perms = set([''.join(p) for p in
                        permutations(string, int(number))])
            lis4 = list(set(lis1).intersection(perms))
            for words in sorted(lis4):
                print(words)
            print(".")
    else:
        sys.exit()

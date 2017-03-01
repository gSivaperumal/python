
import re
word = 'tprs'
string = 'testthisprogram'
prog = re.compile('.+'.join([re.escape(letter) for letter in sorted(word)]))
result = prog.match(sorted(string))
print(result)
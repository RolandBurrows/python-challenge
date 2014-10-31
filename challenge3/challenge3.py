#http://www.pythonchallenge.com/pc/def/equality.html
print 'Challenge 3 Results'
print '-------------------'

import re

input_file = open('challenge3input.txt','rb')
pattern = re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', input_file.read())
print ''.join(pattern)

#Solution:
#http://www.pythonchallenge.com/pc/def/linkedlist.html
#http://www.pythonchallenge.com/pc/def/linkedlist.php

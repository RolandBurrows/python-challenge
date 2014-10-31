#http://www.pythonchallenge.com/pc/def/linkedlist.php
print 'Challenge 4 Results'
print '-------------------'

import urllib2
import re

starting_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
url = urllib2.urlopen(starting_url)

i = 1
print i, '12345'

while i <= 400:
    text = url.readlines()
    str = ''.join(text)
    print i, str
    number = re.findall(r'\d+', str)
    str_number = ''.join(number)
    new_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % (str_number,)
    if str_number == '16044':
        print 'SHIFT IN PATTERN DETECTED'
        new_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'
    if str_number == '8268363579':
        print 'SHIFT IN PATTERN DETECTED'
        new_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579'
    url = urllib2.urlopen(new_url)
    i+=1

#Solution:
#Iteration 250 'peak.html'
#http://www.pythonchallenge.com/pc/def/peak.html

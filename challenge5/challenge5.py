#http://www.pythonchallenge.com/pc/def/peak.html
#http://www.pythonchallenge.com/pc/def/pickle.html
print 'Challenge 5 Results'
print '-------------------'

import pickle

input_file = open('banner.p','rb')
new_file = pickle.load(input_file)
#print new_file
for item in new_file:
    print "".join(char[0] * char[1] for char in item)

#Solution:
#http://www.pythonchallenge.com/pc/def/channel.html

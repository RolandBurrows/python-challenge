#http://www.pythonchallenge.com/pc/def/ocr.html
print 'Challenge 2 Results'
print '-------------------'

from collections import Counter

#>>> Given the input data from the page source...
input_file = open('challenge2input.txt','r')
input_data = input_file.read()
#>>> Print the characters and their counts
print Counter(input_data)

#Unique characters: aeilquty
#In actual order of discovery: equality

#Solution:
#http://www.pythonchallenge.com/pc/def/equality.html

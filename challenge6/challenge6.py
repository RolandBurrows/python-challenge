#http://www.pythonchallenge.com/pc/def/channel.html
print 'Challenge 6 Results'
print '-------------------'

import zipfile
import re

channel_zip = zipfile.ZipFile('channel.zip','r')
starting_file = channel_zip.open('90052.txt','r')
starting_file_name = '90052.txt'
input_file = starting_file
file_name = starting_file_name
output_file = open('comments_output.txt','w')

i = 1
print i, '90052', file_name

while i <= 1000:
    i+=1
    file_contents = input_file.read()
    file_comments = channel_zip.getinfo(file_name).comment

    if file_contents == 'Collect the comments.':
        break
    
    content_digits = re.findall(r'\d+', file_contents)[0]
    file_name = ''.join(content_digits+'.txt')
    #print i, file_contents, file_comments
    output_file.write(file_comments)
    
    input_file = channel_zip.open(content_digits+'.txt','r')

output_file.close()

#Solution:
#http://www.pythonchallenge.com/pc/def/hockey.html
#http://www.pythonchallenge.com/pc/def/oxygen.html

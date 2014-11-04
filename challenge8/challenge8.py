#http://www.pythonchallenge.com/pc/def/integrity.html
print 'Challenge 8 Results'
print '-------------------'

import bz2

username_code = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
password_code = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

username_string = bz2.decompress(username_code)
password_string = bz2.decompress(password_code)
 
print username_string, password_string
#huge file

#Solution:
#http://www.pythonchallenge.com/pc/return/good.html

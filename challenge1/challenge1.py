#http://www.pythonchallenge.com/pc/def/map.html
print 'Challenge 1 Results'
print '-------------------'

import string

#Given the input string...
input_string1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#And the hint that letters should be phase-shifted 2 letters forward
trans_table = string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
transmuted_string = string.translate(input_string1, trans_table)
#The transmuted string is...
print transmuted_string

#Indicating that the URL string needs to be edited with...
input_string2 = 'map'
transmuted_string2 = string.translate(input_string2, trans_table)
print
print transmuted_string2

#Solution:
#http://www.pythonchallenge.com/pc/def/ocr.html

#http://www.pythonchallenge.com/pc/def/oxygen.html
print 'Challenge 7 Results'
print '-------------------'

import Image   #Requires installing the Python Imaging Library
import re

input_image = Image.open("oxygen.png")
#Rectangle centers are at 47 pixels down, with each being 7 pixels wide.  Width of all rectangles = 609 pixels.
color_samples = [input_image.getpixel((x, 47)) for x in range(0, 609, 7)]
#print color_samples
#Each color sample has equal RGB values, so extract the R value only
r_values = [r for r, g, b, w in color_samples]
print r_values
print "".join(map(chr, map(int, r_values)))
print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, r_values))))))

#Solution:
#http://www.pythonchallenge.com/pc/def/integrity.html

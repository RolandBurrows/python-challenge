#http://www.pythonchallenge.com/pc/return/5808.html
print 'Challenge 11 Results'
print '-------------------'

import Image

input_image = Image.open("cave.jpg")
image_size = list(input_image.size)
image_size[0] /= 2
image_size[1] /= 2
#Shrink the image to half-size and resample with NEAREST to only keep even columns
shrink_image = input_image.resize(image_size, Image.NEAREST)
shrink_image.save("evens.png")

#Solution:
#http://www.pythonchallenge.com/pc/return/evil.html

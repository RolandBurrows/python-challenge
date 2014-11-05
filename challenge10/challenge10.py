#http://www.pythonchallenge.com/pc/return/bull.html
print 'Challenge 10 Results'
print '-------------------'

i = 0
j = 0
sequence = [1]
char_count = 1
result = []
 
while i < 30:
    print i,':', len(sequence)
    num_length = len(sequence)
    while j < (num_length - 1):
        if sequence[j] == sequence[j + 1]:
            char_count += 1
        else:
            result.append(char_count)
            result.append(sequence[j])
            char_count = 1
        j += 1
 
    result.append(char_count)
    result.append(sequence[j])
    sequence = result
    result = []
    char_count = 1
    j = 0
    i += 1
 
print i,':', len(sequence)
#len(a[30])= 5808

#Solution:
#http://www.pythonchallenge.com/pc/return/5808.html

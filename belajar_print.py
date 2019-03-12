"""Few print example commonly use"""

#Basic use print
print('Hello World')
#Hasil-> Hello World

#Basic with variable
value = 'Hello World'
print(value)
#Hasil-> Hello World

#Basic with formating
value0 = 'Hello'
value1 = 100
value2 = 0.1
print('%s %d %f' % (value0, value1, value2))
#Hasil-> Hello 100 0.100000
print('{} {} {}'.format(value0, value1, value2))
#Hasil-> Hello 100 0.1
print('{1} {0} {2}'.format(value0, value1, value2))
#Hasil-> 100 Hello 0.1

#more style: https://pyformat.info/


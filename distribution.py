"""
distribution.py
Author: Peter Bynum
Credit: Mr. Dennison's sorting system
Making lists lowercase: http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python
Assignment: Character Distribution

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""

s = input("Please enter a string of text (the bigger the better): ")
print('The distribution of characters in "{0}" is:'.format(s))
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
arev = list(a[::-1])
anum = []
anum1 = []
s = s.lower()

for i in range(0,26):
    anum.append(s.count(arev[i]))

sorted = False

def compare(x, y):
    return x > y

while not sorted:
    for j in range(0,25):
        if compare(anum[j], anum[j+1]):
            anum[j], anum[j+1] = anum[j+1], anum[j]
            arev[j], arev[j+1] = arev[j+1], arev[j]
            anum1 = list(anum)
            anum1.sort()
            if anum == anum1:
                sorted = True
        else:
            anum1 = list(anum)
            anum1.sort()
            if anum == anum1:
                sorted = True


for i in range(0,25):
    if anum[25-i]>0:
        print(arev[25-i]*anum[25-i])




"""
goes through alphabet and switches when > or <

def compare(s.count[i], s.count[i+1]):
    return b > a

for i in range(0,25):
    if 

def compare(s.count[i], b):
    return b > a


def bsort(seq, compare):
    sorted = False  # assume the seq is not sorted to start with
    while not sorted:
        sorted = True   # assume it's already sorted correctly
        for index, value in enumerate(seq): # for every element in seq
            if index > 0:                   # past the first..
                if not cmp(seq[index-1], value):  # if this element is out of order
                    sorted = False          # then the list is not sorted yet
                    seq[index-1], seq[index] = seq[index], seq[index-1] # and swap it


tosort = [4, 10, 3, -1000, 30]
bsort(tosort, compare)
print(tosort)
"""





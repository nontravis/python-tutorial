l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in l:
    print num


for num in l:
    if num % 2 == 0:
        print num

for letter in "This is a string.":
    print letter

# tuple
l = [(2, 4), (6, 8), (10, 12)]
for (t1, t2) in l:
    print t1

# dictionaries
d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print item

for k, v in d.iteritems():          # NOTE: python 2 - returns a list of tuples
    print k
    print v
# NOTE: items() allow to use in python 2
#       but built a real list of tuples and returned that.
#       That could potentially take a lot of extra memory.

# For Python 3
for k, v in d.items():              # NOTE: like iteritems() in python 2
    print(k)
    print(v)

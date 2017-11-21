# map()
# filter()
# reduse()
# enumerate()
# all() and any()
# complex()

#┌───────────────────────────────┐
#│ NOTE: map(function, sequence) │
#└───────────────────────────────┘
items = [1, 2, 3, 4, 5]
square = map(lambda x: x**2, items)
square = map(square, items)

a = [1, 2, 3]
b = [4, 5, 6]
map(lambda x, y: x + y, a, b)


def multiply(x): return (x * x)


def add(x): return (x + x)


funcs = [multiply, add]
for i in range(5):
    print map(lambda x: x(i), funcs)


#┌──────────────────────────────────┐
#│ NOTE: filter(function, sequence) │
#└──────────────────────────────────┘
number_list = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, number_list)
print(less_than_zero)


# NOTE: reduce(function, sequence)
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])


#┌───────────┐
#│ NOTE: zip │
#└───────────┘
def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)


x = [1, 2, 3]
y = [4, 5, 6]
zip(x, y)

a = [1, 2, 3, 4, 5]
b = [2, 2, 10, 1, 1]

for pair in zip(a, b):
    print max(pair)

map(lambda pair: max(pair), zip(a, b))

# shorter
x = [1, 2, 3]
y = [4, 5, 6, 7, 8]
zip(y, x)

# dictionary
d1 = {'a': 1, 'b': 2}
d2 = {'c': 4, 'd': 5}
zip(d1, d2)
zip(d1.itervalues(), d2)


#┌──────────────────────────────────────┐
#│ NOTE: enumerate() ==> tracking count │
#└──────────────────────────────────────┘
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


l = ['a', 'b', 'c']
for count, item in enumerate(l):
    if count >= 2:
        break
    else:
        print item


#┌───────────────────────┐
#│ NOTE: all() and any() │
#└───────────────────────┘
def all(iterable):          # is all true?
    for element in iterable:
        if not element:
            return False
    return True


def any(iterable):          # is true at least one?
    for element in iterable:
        if element:
            return True
    return False


#┌─────────────────┐
#│ NOTE: complex() │
#└─────────────────┘
complex(10, 2)
complex("10+2j")

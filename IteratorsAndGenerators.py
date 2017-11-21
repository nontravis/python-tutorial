# def function
# generator function ==> save memory, is iterator
#                        Using yield anywhere in a function makes it a generator.

# NOTE: def function
# def gencubes(n):
#     out = []
#     for num in range(n):
#         out.append(num**3)
#         return out            # NOTE: hold all entire list in memory


# NOTE: generator function
def gencubes(n):
    for num in range(n):
        yield num**3        # NOTE: only keep track of the current number in that sequence


for x in gencubes(10):
    print x


def genfibon(n):
    a, b = 1, 1
    for i in xrange(n):
        yield a
        a, b = b, a + b


for num in genfibon(10):
    print num


# NOTE: next()
def simple_gen():
    for x in xrange(3):
        yield x


g = simple_gen()        # is iterator can use next(iter)

next(g)                 # until it raises a StopIteration exception,
                        # signaling that all values have been generated


# NOTE: iter()
s = "hello"

for let in s:
    print let

s_iter = iter(s)
next(s_iter)

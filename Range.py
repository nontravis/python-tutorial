l = range(0, 10)            # NOTE: not include 10
type(l)

step = range(0, 10, 2)
step

# NOTE:
# Generators -  allow the generation of "generated" object that are provided at that instant
#               but not store every instance generated into memory
# python2 - built-in range generator called xrange()
# python3 - range() = xrange()

for num in xrange(1, 10000):
    print num

x = xrange(1, 6)
type(x)  # NOTE: not return list but it's generator
list(x)

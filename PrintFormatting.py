from __future__ import print_function

print("This is a string")

s = 13.13

# NOTE: Conversion Format methods
print("Place my variable here: %s" % (s))
print("Floating point number: %10.3f" % (13.145))

print("Covert to string %s" % (123))  # or %r
print("First: %s, Second: %s, Third %s" % ("hi!", "two", 3))

print("First: {x}, Second: {y}, Third {x}".format(x="inserted", y="two!"))  # NOTE: reccomend

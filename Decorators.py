
# NOTE: Scope Review
s = "This is a global variable."


def func():
    return locals()


locals()
globals()           # all avaliable global var right now
globals().keys()
globals()["s"]


def hello(name="Jose"):
    return "Hello " + name


greet = hello   # NOTE: everythings in python is _object_
del hello
greet()         # NOTE: still working


# NOTE: Functions within functions

def helloName(name="Jose"):
    print "The helloName() function has been executed"

    def greet():
        return "\tThis is inside the greet() function"

    def welcome():
        return "\tthis is inside the welcome() function"

    if name == "Jose":
        return greet
    else:
        return welcome


x = helloName()

try:
    2 + "2"
except TypeError:
    print "There was a type error!"
finally:
    print "Finally this was printed"

try:
    f = open("testException", "w")
    f.write("test write this")
except IOError:
    print "Error in writing to the file!"
else:
    print "File writ was a success"     # NOTE: if no exception will call
finally:
    print "Always execute finally code blocks!"


def ask_int():
    while True:
        try:
            val = int(raw_input("Please enter an integer: "))
        except ValueError:
            print "Looks like you did not enter an integer!"
            continue
        else:
            print "Correct, that is an integer!"
            break

        print val


ask_int()

'Hello'
'This is also a string.'  # sequence
"This is a string."  # string

"I'm a string"
' "This is a quote" '


#┌────────────────┐
#│ NOTE: Printing │
#└────────────────┘
print 'Hello World 1'
print 'Hello World 2'           # this is look like a statement

print 'Here is a new line\nand here is the second line.'

from __future__ import print_function
print("Hello world")            # python 2: print look like a function

len("Hello World")


#┌────────────────┐
#│ NOTE: StringIO │
#└────────────────┘
# NOTE: The StringIO module implements an in-memory file like object.
#       This object can then be used as input or output to most functions
#       that would expect a standard file object.
import StringIO
import cStringIO

message = "This is just a normal string."

f = cStringIO.StringIO(message)

f.read()
f.write(" Second line written to file like object")
f.seek(0)
f.read()
f.getvalue()


#┌────────────────┐
#│ NOTE: Indexing │
#└────────────────┘
s = "Hello World"
s[0]
s[1]
s[1:]
s[:1]
s[:3]
s[:]
s[-1]

s[::1]
s[::2]
s[::-1]

s[1] = "h"  # immutability
s + " concat string"
s * 5

#┌─────────────────────────┐
#│ NOTE: Build-in function │
#└─────────────────────────┘
s = "Hello world"

s.center(20, 'z')

print "hello\thi"
"hello\thi".expandtabs()

s.isalnum()  # alphanumeric == [a-zA-z0-9]
"Hello123".isalnum()
s.isalpha()  # alphabetic == [a-zA-z]
"Hello123".isalpha()
"Hello".isalpha()
"สวัสดี".isalpha()

"Hello".islower()
"Hello".isupper()
"Hello".istitle()
"Hel lo".isspace()
"\n\r\t ".isspace()
"".isspace()
"Hello".endswith("o")
"Hello".startswith("H")

s.partition('e')  # similar split but not remove split param string
s.upper()
s.lower()
s.split()
s.split('e')


import string
string.ascii_letters        # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.octdigits            # '01234567'
string.digits               # '0123456789'
string.hexdigits            # '0123456789abcdefABCDEF'
string.whitespace           # '\t\n\x0b\x0c\r '
string.punctuation          # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# ''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
string.printable


#┌───────────────┐
#│ NOTE: Justify │
#└───────────────┘
'Hello'.rjust(10)
'Hello'.rjust(10, "-")
'Hello'.rjust(20)
'Hello'.ljust(10)
'Hello'.center(20)


#┌──────────────────┐
#│ NOTE: Whitespace │
#└──────────────────┘

spam = '    Hello World     '
spam.strip()
spam.lstrip()
spam.rstrip()

spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')


#┌──────────────────┐
#│ NOTE: Copy Paste │
#└──────────────────┘
# send text to and receive text from your computer’s clipboard
import pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste()

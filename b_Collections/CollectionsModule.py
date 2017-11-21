#┌───────────────────────────────────────────┐
#│ NOTE: Counter() is dictionaries sub class │
#└───────────────────────────────────────────┘
from collections import Counter


l = [1, 1, 2, 3, 2, 2, 4, 5, 5, 6, 7, 7, 7]
Counter(l)


s = "aaasssdddffggvvdsstt"
Counter(s)

s = "How many times does each word show up in this sentence word times each each word"
words = s.split()
c = Counter(words)
c.most_common(3)

sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
# c.most_common()[:-n - 1:-1]     # n least common elements
c += Counter()                  # remove zero and negative counts


#┌────────────────────────────────────┐
#│ NOTE: defaultdict(<default_value>) │
#└────────────────────────────────────┘
# init default value and no key error
from collections import defaultdict

d = {"k1": 1}
d["k1"]
d["k2"]         # throw exception

d = defaultdict(object)
d['one']

for item in d:
    print item

d = defaultdict(lambda: 0)
d["one"]
d["two"] = 2


#┌─────────────────────┐
#│ NOTE: OrderedDict() │
#└─────────────────────┘
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for k, v in d.iteritems():       # NOTE: don't get order
    print k, v

from collections import OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
for k, v in d.iteritems():
    print k, v

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2
d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1
d1 == d2


#┌────────────────────┐
#│ NOTE: namedtuple() │
#└────────────────────┘
# a very quick way of creating a new object/class type with some attribute fields.

from collections import namedtuple

Dog = namedtuple("Dog", 'age breed name')           # (class_name, attr_name)
Dog = namedtuple("Dog", ["age", "breed", "name"])

sam = Dog(age=2, breed="Lab", name="Sammy")

sam[0]
sam[1]
type(sam)

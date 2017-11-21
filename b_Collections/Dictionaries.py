# NOTE:
# Dictionaries are mappings and do not retain order!
# Mappings are a collection of objects that are _stored by a key_,
# unlike a sequence that stored objects by their relative position.

my_dict = {"key1": "value", "key2": "value2"}
my_dict["key1"]

my_dict = {"k1": 123, "k2": 3.4, "k3": "string"}
my_dict["k3"][2]
my_dict["k1"] += 50

d = {}
d["animal"] = "Dog"

d = {"k1": {"nest_key": {"sub_nest_key": "value"}}}
d["k1"]["nest_key"]["sub_nest_key"]


# NOTE: operator
d = {"k1": 1, "k2": 2, "k3": 3}
d.values()
d.items()           # tuple


d = {"k1": 1, "k2": 2}


for k in d.iteritems():
    print k

for k in d.iterkeys():
    print k

d.viewitems()   # if you have a large dict be careful to calling this
d.viewkeys()    # because you may just get a huge output
d.viewvalues()

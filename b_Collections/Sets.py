l = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
l = set(l)

# NOTE: add
s = set()
s.add(1)
s.add(2)
s.add(2)

# NOTE: clear
s.clear()

# NOTE: copy
sc = s.copy()

# NOTE: discard
s = {1, 2, 3}
s.discard(2)    # if not found will ignore

# NOTE: difference
s = {1, 2, 3}
sc = {1, 2, 4}
s.difference(sc)    # base on "s"
sc.difference(s)    # base on "sc"
sc.difference_update(s)     # base on intersec items form "sc"

# NOTE: intersection
s1 = {1, 2, 3}
s2 = {1, 2, 4}
s1.intersection(s2)
s1.intersection_update(s2)

# NOTE: symmetric => opposite intersection
s1 = {1, 2, 3}
s2 = {1, 2, 4}
s1.symmetric_difference(s2)

# NOTE: union
s1 = {1, 2, 3}
s2 = {1, 2, 4}
s1.union(s2)


# NOTE: update
s1 = {1, 2, 3}
s2 = {1, 2, 4}
s1.update(s2)


# NOTE: isdisjoint = Is it not intersection?
s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}
s1.isdisjoint(s2)
s1.isdisjoint(s3)

# NOTE: issubset
s1.issubset(s2)
s1.issubset(s3)

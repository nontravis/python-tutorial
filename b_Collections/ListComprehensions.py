l = []
for letter in "word":
    l.append(letter)
print l

l = [letter for letter in "word"]

l = [x**2 for x in xrange(0, 11)]

l = [number for number in xrange(11) if number % 2 == 0]

celsius = [0, 10, 20.1, 34.5]
fahrenheit = [(temp * (9 / 5.0) + 32) for temp in celsius]

l = [x**2 for x in [x**2 for x in xrange(0, 11)]]       # x**4


{x: x**2 for x in range(10)}

{k: v**2 for k, v in zip(['a', 'b'], xrange(2))}

$ python -m timeit 'for i in range(1000000):' ' pass'
10 loops, best of 3: 90.5 msec per loop
$ python -m timeit 'for i in xrange(1000000):' ' pass'
10 loops, best of 3: 51.1 msec per loop
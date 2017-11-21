import timeit
import time

# 0-1-2-3-4-5-...-99
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)  # run 10000 times
timeit.timeit('"-".join(str(n) for n in xrange(100))', number=10000)  # run 10000 times


# start = timer()
start = time.time()
for i in range(10000):
    "-".join(str(n) for n in xrange(100))
# end = timer()
end = time.time()
print(end - start)


timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)  # run 10000 times
timeit.timeit('"-".join([str(n) for n in xrange(100)])', number=10000)  # run 10000 times

timeit.timeit('"-".join(map(str,range(100)))', number=10000)  # run 10000 times
timeit.timeit('"-".join(map(str,xrange(100)))', number=10000)  # run 10000 times

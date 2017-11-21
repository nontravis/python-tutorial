
#┌───────────┐
#│ NOTE: pdb │
#└───────────┘
import pdb

x = [1, 3, 4]
y = 2
z = 3

result = y + z
print result

pdb.set_trace()

result2 = y + x
print result2


#┌───────────────┐
#│ NOTE: Logging │
#└───────────────┘
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

import logging
logging.disable(logging.CRITICAL)   # disable critical level _and lower_
logging.basicConfig(
    filename="my_logging.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s")


def factorial(n):
    logging.debug("Start of factorial({0})".format(n))
    total = 1
    for i in xrange(1, n + 1):
        total *= i
        logging.debug("i is {0}, total is {1}".format(i, total))
    logging.debug("Return value is {0}".format(total))
    return total


print(factorial(5))

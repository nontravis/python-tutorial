x = 0

while x < 10:
    print 'x is currently: ', x
    print ' x is still less than 10, adding 1 to x'
    x += 1

else:
    print 'All Done!'


x = 0

while x < 10:
    print 'x is currently: ', x
    print ' x is still less than 10, adding 1 to x'
    x += 1
    if x == 3:
        print 'Breaking because x==3'
        break
    else:
        print 'continuing...'
        continue


# break: Breaks out of the current closest enclosing loop.
# continue: Goes to the top of the closest enclosing loop.
# pass: Does nothing at all.

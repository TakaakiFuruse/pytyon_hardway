i = 0
numbers = []

while i < 31:
    numbers.append(i)

    if numbers[-1] % 6 == 0:
        print 'FB'
    elif numbers[-1] % 3 == 0:
        print 'B'
    elif numbers[-1] % 2 == 0:
        print "F"
    else:
        print i

    i = i + 1

    print 'Nubmers', numbers

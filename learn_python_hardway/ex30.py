nums = range(1, 31)

for num in nums:
    if num%6==0:
        print 'FB'
    elif num%2==0:
        print 'B'
    elif num%3==0:
        print 'F'
    else:
        print num


ten_things = "Apples Oranges Crows Telephone Ligth Sugar"

stuff = ten_things.split(' ')
more_stuff = ["day", "night", "song",
              "frisbee", "corn", "banana", "girl", "boy"]

for s in more_stuff:
    if len(stuff) < 10:
        print "adding", s
        stuff.append(s)
        print "%d items now" % len(stuff)

print "stuff", stuff
print stuff[1]
print stuff[-1]
print stuff.pop()
print ''.join(stuff)
print '#'.join(stuff[3:5])
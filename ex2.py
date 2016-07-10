from sys import argv

script, user_name = argv
prompt = '>'

print "your name is %s" % (user_name)
print "your age?"
age = raw_input(prompt)

print "height?"
tall = raw_input(prompt)

print "nationality?"
nat = raw_input(prompt)

print """
age is %r
tall is %r
nationality is %r
""" % (age, tall, nat)

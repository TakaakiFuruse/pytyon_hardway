# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

in_file = open(from_file).read()

print "input file has %d bytes" % len(in_file)

print "out put file exists? %r" % exists(to_file)
print "ready? yes/no "

input = raw_input()

if input == 'yes':
    out_file = open(to_file, 'w')
    out_file.write(in_file)
    print "Done!"
elif input == 'no':
    print "Aborted!"

out_file.close()
in_file.close()

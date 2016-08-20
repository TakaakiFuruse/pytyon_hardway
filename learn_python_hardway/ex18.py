# -*- coding: utf-8 -*-


def print_two(*args):
    args1, args2, args3 = args
    print "%r %r %r" % (args1, args3, args3)


def print_one(arg):
    print "arg %r" % arg


print_two("one", "one", "one")
print_one("two")

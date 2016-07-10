# -*- coding: utf-8 -*-


def add(a, b):
    print "adding: %d + %d" % (a, b)
    return a + b


def subtract(a, b):
    print "subtracting %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "multiply %d * %d" % (a, b)
    return a * b


def devide(a, b):
    print "dividing %d / %d" % (a, b)
    return a / b

print "function"

ad = add(30, 5)
sub = subtract(78, 4)
mult = multiply(90, 2)
div = devide(100, 2)

print "add %d, sub %d, mult %d, div %d" % (ad, sub, mult, div)

test = add(ad, subtract(sub, multiply(mult, devide(div, 2))))

print test
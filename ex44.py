class Parent(object):
    """docstring for Parent"""
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    """docstring for Chile"""
    def altered(self):
        print "BEFORE OVERRIDE"
        super(Child, self).altered()
        print "AFTER OVERRIDE"

dad = Parent()


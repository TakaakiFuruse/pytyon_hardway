# -*- coding: utf-8 -*-
import re


class Person(object):
    """find out a guy is justin beiber or not"""

    GOOGLE_GUYS = ["Larry Page", "Sergey Brin", "Eric Schmidt"]

    def __init__(self, name):
        self.name = name

    def say_name(self):
        print("my name is " + self.name)

    def is_justin_beiber(self):
        if self.name == "Justin Beiber":
            print "F**K!! YOU ARE BEIBER!!"
        elif re.search("Ninja", self.name):
            print "ニンジャ??? ニンジャナンデ??? ニンジャナンデ????"
        elif self.name in Person.GOOGLE_GUYS:
            print "Hello Mr. %s from google" % self.name
        else:
            print "YOU AREN'T BEIBER!! COOL!!"

    def greet_google_directors(self):
        for name in Person.GOOGLE_GUYS:
            print "Hello " + name

    def greet_ninja_way(self):
        if re.search("Ninja", self.name):
            print "ドーモ､%s=サン" % self.name
        else:
            print "ドーモ"


for line in open("sample.txt"):
    chomped = line.rstrip()
    greet = Person(chomped)
    greet.say_name()
    greet.is_justin_beiber()
    print '-----------------'

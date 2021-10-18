#!/usr/bin/env python

print "Content-Type: text/plain"
print
import random
mod = 1999
value = random.randint(1000+mod, 99999999)
print value


while value %mod != 0:
    value -= 1

print "Random value is " + str(value);

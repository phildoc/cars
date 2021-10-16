#!/usr/bin/env python

import random

print "Content-Type: text/plain"
print
##value = random.randint(10000+10, 99999999)
##print value
##
##while value %10 != 0:
##    value -= 1
##
##print "Random value is " + str(value);

print '<html>'
print '<head>'
print '<title>test Python dynamic html</title>'
print '</head>'
print '<body>'
value = random.randint(10000+10, 99999999)
print value

while value %10 != 0:
    value -= 1
<p>print "Random value is " + str(value);</p>
print '</body>'

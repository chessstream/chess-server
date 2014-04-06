#!/usr/bin/python

import sys
import lib

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print sys.argv[0]

if len(sys.argv) == 3:
    lib.start_game(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 4:
    lib.process_input(sys.argv[1], sys.argv[2], sys.argv[3])

else:
    print 'This command requires 2 or 3 arguments'

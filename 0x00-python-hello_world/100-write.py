#!/usr/bin/python3
import sys
message = "and that piece of art is useful - Dora Korpar, 2015-10-19"
# write message to stderr
sys.stderr.write("{}".format(message))
sys.exit(1)

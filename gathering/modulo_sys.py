# -*- coding: utf-8 -*-

import sys
print "Script: ", sys.argv[0]

if len(sys.argv) > 1:
	print " params", len(sys.argv) -1
	for arg in sys.argv[1:]:
		print arg
else:
	print "No params."

print "------------------------"
print "Imported modules: " + str(sys.modules.keys())

print "------------------------"
print "Ayuda..." +help(sys)
def exitcustom():
	print "Exiting..."

sys.exitfunc = exitcustom
sys.exit()

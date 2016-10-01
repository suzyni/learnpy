from sys import argv
#from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

#with open(from_file) as out_file:
#    with open(to_file, 'w') as in_file:
#        in_file.write(out_file.read())

indata = open(from_file).read()
open(to_file, 'w').write(indata)

# we could do these two on one line too, how?
#in_file = open(from_file)
#indata = in_file.read()
#indata = open(from_file).read()
#print "%s" % indata

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

#out_file = open(to_file, 'w')
#out_file.write(indata)

#print "Alright, all done."

#out_file.close()
#in_file.close()
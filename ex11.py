#print "How old are you?",
#age = raw_input()
#print "How tall are you?",
#height = raw_input()
#print "How much do you weight?",
#weight = raw_input()

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
	
x = age + height + weight
print x

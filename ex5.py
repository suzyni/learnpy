name = "Zed A. Shaw"
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (
    age, height, weight, age + height + weight) 
	
cen_height = height * 2.54
kilo_weight = weight * 0.45
print "%d inches equal to %.2f centermeters, and %d lbs equal to %.2f kilograms" % (height, cen_height, weight, kilo_weight)
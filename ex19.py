def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables form our script:"
cheese_count = 10
amount_of_crackers = 50
cheese_and_crackers(cheese_count, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(cheese_count + 100, amount_of_crackers + 100)

print "What does a function returns? %r" % cheese_and_crackers(20, 30)

def ask_cheese():
    print "How many cheeses do you have?"
    cheese_count = raw_input()
    print "So %d cheeses you have!" % int(cheese_count)

ask_cheese()
i = 0
numbers = []

def app_num(max, increment):
    i = 0
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)
    
        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

app_num(8, 3)

app_num(20, 2)

#print "globle i = %d" % i
print "The numbers: "

for num in numbers:
    print num,
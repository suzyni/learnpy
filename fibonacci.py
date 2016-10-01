#l = [0,1]
#print l[0], '\n', l[1]
#while l[1] < 100:
#    l.append(l[0] + l[1])
#    l.pop(0)
#    print l[1]

#fib = lambda n: reduce(lambda x, y: [x[1], x[0]+x[1]], range(n), [0, 1])[0]

def fib(a = 0, b = 1):
    while True:
        yield a
        a, b = b, a + b

fibgenerator = fib()

for i in range(20):
    print(fibgenerator.next())
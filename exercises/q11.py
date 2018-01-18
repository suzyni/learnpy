# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

l = [x for x in raw_input("> ").split(',')]
results = []
for x in l:
    if int(x, 2) % 5 == 0:
        results.append(x)
print ','.join(results)
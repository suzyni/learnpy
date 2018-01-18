# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

l = [x for x in raw_input("> ").split(' ')]
l = list(set(l))
l.sort()
print ' '.join(l)

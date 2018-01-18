# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
list = [w for w in raw_input("> ").split(',')]
list.sort()
print ','.join(list)
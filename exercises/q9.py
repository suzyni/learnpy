# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
lines = []
while True:
    line = raw_input("> ")
    if line:
        lines.append(line.upper())
    else:
        break

print '\n'.join(lines)
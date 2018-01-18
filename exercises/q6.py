# Question 6
print reduce(lambda x,y: x+","+y, map(lambda d: str(int(round(((2*50*int(d))/30)**(0.5)))), raw_input("> ").split(',')))
print("How old are you?")
age = input()
print("How tall are you?")
height = input()
print("How much do you weigh?")
weight = input()

print(f"So you are {age} years old, {height} tall and {weight} heavy")

# input([prompt])

# If the prompt argument is present, it is written to standard output without a trailing newline. 
# The function then reads a line from input, converts it to a string (stripping a trailing newline), 
# and returns that. When EOF is read, EOFError is raised.
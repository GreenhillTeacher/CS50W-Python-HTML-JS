# NAme
# Having fun with LOOPS
#Learn how to resize our programs
#ASking the user for values
# is requesting via console for something the default is a string
# type casting
begin =7
lines= int(begin)
for line in range(lines):
    for number in range(begin-line,0,-1):
        print(number, end=' ')
    print()

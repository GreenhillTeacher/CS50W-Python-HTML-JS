# print("1 2 3 4 5 6 7 8 9")
#
# print("1\n"+"2\n"+"3\n"+"4\n")
# print("1\n")
# print("2 2\n")
# print("3 3 3\n" )

# for i in range(10): # value from 0 to value-1
#     print (i)
# for j in range(1,10): #first value is included, the second is not
#     print (j, end = '')
#     print (" ", end= '')
# print()
# print("I am done")
# print("...")
#nested loops
for line in range(1,10):  # to control the line
    print()
#BOTH LOOPS USES LINE TO CONTROL THE NUMBERS
    for space in range(9-line):    # Control the space
        print(" ", end='')
    for number in range(line):
        print(line, end='')
    print(end=' ')
    for number in range(line):
        print(line, end='')

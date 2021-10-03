# first option
import re

string = input("Please enter a binary number: ")

print( len(re.findall("1", string)))

# second option

def calculatePositives(string):
    count = 0
    for char in string:
        if(char == "1"):
            count += 1

    return count


print(calculatePositives(string))
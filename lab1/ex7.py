import re


string = input("Please enter a string that has a number: ")
print(re.findall("\d+", string)[0])
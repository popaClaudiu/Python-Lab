def getFrequencies(string):
    frequencies = {}

    for char in string:
        if char.isalpha():
            if(frequencies.get(char)):
                frequencies[char] += 1
            else: 
                frequencies[char] = 1
    return frequencies

def maxFrequency(string):
    frequencies = getFrequencies(string)
    letter = max(frequencies, key=frequencies.get)
    return letter


string = input("Please enter a string: ")
print(maxFrequency(string.lower()))
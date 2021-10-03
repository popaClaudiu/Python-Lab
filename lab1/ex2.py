string = input("Please enter a string:");

def calculateVowals(word):
    count = 0 
    vowals = "aeiou"
    for letter in word: 
        if letter in vowals:
            count += 1
    return count


print(calculateVowals(string.lower()));
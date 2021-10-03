
def reverse(number):
    reversedNum = 0
    while(number > 0):
        digit = number % 10
        reversedNum = (reversedNum * 10) + digit
        number = number // 10

    return reversedNum

def isPalindrom(number):
    return number == reverse(number)

number = int(str(input("Please insert a number: ")));
print(isPalindrom(number))
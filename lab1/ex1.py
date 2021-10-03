

def gcd(a, b):
    if(b == 0):
        return a

    return gcd(b, a%b)


def gcd_multiple(numbers):
    if len(numbers) == 1:
        return numbers[0]

    result = numbers[0]
    for nr in numbers[1:]:
        result = gcd(result, nr)

    return result

numbers =  list(map(int, input("Enter multiple values: ").split()))
print(gcd_multiple(numbers))
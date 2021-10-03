string = input("Please enter a camelCase string: ")


def snake_case(word):

    result = [word[0].lower()]

    for char in word[1:]:
        if char.isupper():
            result.append('_' + char.lower())
        else:
            result.append(char)

    return ''.join(result)


print(snake_case(string))
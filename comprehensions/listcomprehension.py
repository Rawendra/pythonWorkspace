fruits = ['apple', 'mnago', 'banana']


def getFirstLetter(fruit):
    result = fruit[0:1]
    return result


result = [getFirstLetter(fruit) for fruit in fruits]
print(result)

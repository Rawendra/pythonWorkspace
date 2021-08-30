my_string = 'this is my first string'

# multiple string

my_new_string = '''this is new string
    which spreads across multiple rows
    like this one'''

#index in string

# first character
print(my_string[0])

# printing the last character
print(my_string[-1])

# gettting all indices
lenghtOfString = len(my_string)
print(lenghtOfString)

# finding the index of character in string
print(my_string.index('s'))

# finding the count of a character in string
print(my_string.find('string'))

# printing the lower case
print(my_string.lower())

# printing the uppercase
print(my_string.upper())

# starts with / ends with

print(my_string.startswith('this'))
print(my_string.endswith('string'))

# strip
c = '#### this is so awesome ###'

c = c.strip('#')
print(c)
# striping the empty space at the begining and end
print(c.strip())

# replace
d = 'I have a new message where spaces are replaced with empty space'
print(d.replace(' ', ''))


e='getting the list of words from a single string'
print(e.split(' '))

#creating a string with a common delimiter
f=['apple','mango','banana']
print('_'.join(f))#using blank space to join the elements of f, f is a list


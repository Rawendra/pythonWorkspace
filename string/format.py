#format method of string
name='Rawendra'
age=28
salary=24000

my_string='my name is {}, my age is {}, I earn {}'.format(name,age,salary)
print(my_string)


my_string='my name is {0}, my age is {1}, I earn {2}, yes my age is {1}'.format(name,age,salary)
print(my_string)
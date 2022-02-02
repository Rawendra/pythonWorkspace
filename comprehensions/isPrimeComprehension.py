from math import sqrt


def isPrime(num):
    if(num < 2):
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True


number = int(input('enter the number :'))
print('printing the primes less than -->{}'.format(number))
primes = [x for x in range(number) if isPrime(x)]
print(primes)

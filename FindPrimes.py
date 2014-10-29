__author__ = 'Anand Patel'

"Finds all primes less than or equal to the input number."

def findPrimes(n):
    for i in range(2, n+1):
        if testPrime(i):
            print i,


def testPrime(t):
    for i in range(2, t):
        if i < t:
            if (t % i) == 0:
                return False
    return True


findPrimes(input("Enter the number you want to find primes up to: "))




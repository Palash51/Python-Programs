# Prime Number Sieve
 2. # http://inventwithpython.com/hacking (BSD Licensed)
 3.
 4. import math
 5.
 6.
 7. def isPrime(num):
 8.     # Returns True if num is a prime number, otherwise False.
 9.
10.     # Note: Generally, isPrime() is slower than primeSieve().
11.
12.     # all numbers less than 2 are not prime
13.     if num < 2:
14.         return False
15.
16.     # see if num is divisible by any number up to the square root of num
17.     for i in range(2, int(math.sqrt(num)) + 1):
18.         if num % i == 0:
19.             return False
20.     return True
21.
22.
23. def primeSieve(sieveSize):
24.     # Returns a list of prime numbers calculated using
25.     # the Sieve of Eratosthenes algorithm.
26.
27.     sieve = [True] * sieveSize
28.     sieve[0] = False # zero and one are not prime numbers
29.     sieve[1] = False
30.
31.     # create the sieve
32.     for i in range(2, int(math.sqrt(sieveSize)) + 1):
33.         pointer = i * 2
34.         while pointer < sieveSize:
35.             sieve[pointer] = False
36.             pointer += i
37.
38.     # compile the list of primes
39.     primes = []
40.     for i in range(sieveSize):
41.         if sieve[i] == True:
42.             primes.append(i)
43.
44.     return primes
import math
#This is for Problem 1
#bal bla bla
def prob1():
    sum = 0;
    for i in range(1000):
        if(i%3 == 0):
            sum += i
        elif(i%5 == 0):
           sum += i
    print sum

#Problem 2
def fib2(n):    # write Fibonacci series up to n
    a, b = 0, 1
    sumf = 0
    while b < n:
        if((b%2) == 0):
            sumf += b 
        a, b = b, a+b
    return sumf
#Problem 3
def primefact(n,primes):
    factors = []
    i = 0
    p = n 
    while i < len(primes):
        dv = primes[i]
        if(checkdprime(factors,n) == False):
            if(p%dv == 0):
                factors.append(dv)
                p = p/dv
                i = 0
            else:
                i= i+1
        else:
            break
    return factors
#checks if the so far factors add to number factorizing
def checkdprime(l,ck):
    tl = 1
    for i in l:
        tl = tl * i
    if(tl == ck):
        return True
    else:
        return False
#generates primes using sieve of Eratosthenes algorithm
def prime(n):
    numbers = range(n)
    for i in range(2,n):
        p = numbers[i]
        if(p != 0):
            for y in range(2,n):
                if((p*y) < n):
                    numbers[p*y] = 0   
    numbers = filter(lambda x: 1 if x and x>1 else 0,numbers)
    return numbers
#problem 4
def palindrome():
    largest1 = 999
    largest2 = 999
    possible = []
    while largest2 > 0:
        for i in range(largest1,0,-1):
            if(checkpalin(largest2 * i)):
                possible.append(largest2 * i)
        largest2 = largest2 - 1
    print max(possible)
def checkpalin(n):
    l = ''
    p=n
    n = str(n)
    l = n[::-1]
    if(l != n):
        return False
    return True
#problem 5
def problem5():
    n = prime(20)
    total = []
    for i in range(20,1,-1):
        check = primefact(i,n)
        print check
        for j in check:
            if check.count(j) > total.count(j):
                dff =  check.count(j) - total.count(j)
                for d in range(dff):
                    total.append(j)
    return reduce(lambda x,y: x*y, total)

                    
def main():
    #print checkpalin(9119)
    #palindrome()
    #n = prime(21)
    #print primefact(20,n)
    print problem5()
if __name__ == '__main__':
    main()


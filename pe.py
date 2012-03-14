#This is for Problem 1
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
def main():
    answer = fib2(4000000)
    print answer

if __name__ == '__main__':
    main()


#This is for Problem 1
def prob1():
    sum = 0;
    for i in range(1000):
        if(i%3 == 0):
            sum += i
        elif(i%5 == 0):
            sum += i
    print sum
#Global Used
class glb:
    current = 0
    count = 0
    prev = 0
#Problem 2
def fib():
    fib0 = 0
    fib1 = 1
    if (glb.count == 0): 
        glb.count = glb.count +1
        glb.current = fib0
        return fib0
    if (glb.count == 1):
        glb.count = glb.count+1
        glb.prev = fib0
        glb.current = fib1
        return fib1
    if (glb.count == 2):
        next = glb.current + glb.prev
        glb.prev = glb.current
        glb.current = next
        return glb.current
           
    

def evenorodd(n):
    if n%2==0:
        print("given",n,"is even")
    else:
        print("given",n,"is odd")
    return
        
        
def even_N(n):
    for i in range(1,n):
        if i%2==0:
            print(i)
    return
            
            
            
def pos(n):
    if n>0:
        print("given",n,"is positive")
    else:
        print("given",n,"is negative")
    return
        
        
# Python Program to find the factors of a number
def factorsN(n):
    #print("the factors of",n, "are")
    for i in range(1,n+1):
        if n % i == 0:
            print(i)
    return  
            
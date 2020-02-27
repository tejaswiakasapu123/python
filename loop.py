# print reverse of n natural numbers
n=int(input("enter n value: "))
for i in range(n,0,-1):
    print(i)
    
enter n value: 7
7
6
5
4
3
2
1



# Python Program to find the factors of a number
def factors(n):
    print("the factors of",n, "are")
    for i in range(1,n+1):
        if n % i == 0:
            print(i)

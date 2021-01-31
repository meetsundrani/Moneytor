def my_fibo(n):
    a = 0
    b = 1
    if n < 0: 
        print("Invalid input!!!") 
    if n == 0: 
        return a 
    if n == 1: 
        return b 
    else: 
        for i in range(2,n+1): 
            tem = a + b 
            a = b 
            b = tem 
        return b
           
n=int(input())
print(my_fibo(n))
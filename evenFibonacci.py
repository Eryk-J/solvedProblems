fibo = [1,2]
fiboevens = [2]
def evenFibonacci(n):
    for i in range(n-2):
        fibo.append(fibo[i] + fibo[i+1])
        if fibo[-1] % 2 == 0:
            fiboevens.append(fibo[-1])
    print(fiboevens[-1] + fiboevens[-2])

evenFibonacci(10)
print (fibo)
print (fiboevens)
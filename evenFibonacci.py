fibo = [1,2]
fiboevens = [2]
def evenFibonacci(n):
    for i in range(n):
        fibo.append(fibo[i] + fibo[i+1])
        if (fibo[-1] % 2 == 0) and (fibo[-1] < n):
            fiboevens.append(fibo[-1])
        if (fibo[i] + fibo[i+1]) > n:
            break
    print(sum(fiboevens))

evenFibonacci(4000000)

i=[]
def multiplesof3and5(n):
    for n in range(n+1):
        if n%3==0 or n%5==0:
            i.append(n)
    ans=sum(i)
    print(ans)
multiplesof3and5(10)

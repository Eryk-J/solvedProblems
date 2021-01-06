#Prompt
#Print Fizz if divisable by 3
#Print Buzz if divisable by 5
#Print FizzBuzz if both are true
#Print original number otherwise
def Fizz(i):
    if i%3==0 and i%5==0:
        return "FizzBuzz"
    if i%3==0:
        return "Fizz"
    if i%5==0:
        return "Buzz"
    return i

for i in range(1,101):
    print(Fizz(i))

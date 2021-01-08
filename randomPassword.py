import random
yourPass = []
x = 4
charRandomizer = ['0' ,'1','2' ,'3','4' ,'5' ,'6' ,'7','8' ,'9' ,'a' ,'b' ,'c' ,'d' ,'e' ,'f' ,'g' ,'h' ,'i' ,'j' ,'k' ,'l' ,'m' ,'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'v' ,'w' ,'x' ,'y' ,'z' ,'A' ,'B' ,'C' ,'D' ,'E' ,'F' ,'G' ,'H' ,'I' ,'J' ,'K' ,'L' ,'M' ,'N' ,'O' ,'P' ,'Q' ,'R' ,'S' ,'T' ,'U' ,'V' ,'W' ,'X' ,'Y' ,'Z' ,'~' ,'!' ,'@' , '#' ,'$' ,'%' ,"&" ,'.' ,'/' , '<', '>' ,'?']
# 12 character password
def shortPass ():
    for i in range(12):
        yourPass.append(random.choice(charRandomizer))
    print(''.join(str(x) for x in yourPass))
# 14 character password
def mediumPass ():
    for i in range(16):
        yourPass.append(random.choice(charRandomizer))
    print(''.join(str(x) for x in yourPass))
# 20 character password
def longPass ():
    for i in range(20):
        yourPass.append(random.choice(charRandomizer))
    print(''.join(str(x) for x in yourPass))
# custom length password
def customPass ():
    for i in range(userLength):
        yourPass.append(random.choice(charRandomizer))
    print(''.join(str(x) for x in yourPass))
while x > 3:
    cont = input('New password? y or n:')
    if cont == 'y':
        yourPass.clear()
        userChoice = input('Do you want a long(20chars), medium(16chars), short password(12chars) or custom length password?')
        if userChoice == 'long':
            longPass()
        if userChoice == 'short':
            shortPass()
        if userChoice =='medium':
            mediumPass()
        if userChoice =='custom':
            userLength = int(input('length of password?:'))
            customPass()
    else: break



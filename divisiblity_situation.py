n1=int(input('enter divisible no:'))
n2=int(input('enter non divisible no:'))
li=list(range(1,1000))
for k in li:
    if k%n1==0 and k%n2!=0:
        print(k)

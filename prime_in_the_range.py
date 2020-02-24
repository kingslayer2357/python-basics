low=int(input('enter lower limit:'))
upr=int(input('enter upper limit:'))
li=list(range(low,upr+1))
for num in li:
    for i in range(2,num):
        if num%i==0:    
             li=[x for x in li if x!=num]
        else:
            pass
print(li)
    

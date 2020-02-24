li=list(range(1,10000))
low=int(input('enter lower limit:'))
upr=int(input('enter upper limit:'))
for k in li:
    for i in range(low,upr+1):
        if k%i!=0:
            li=[x for x in li if x!=k]
        else:
            pass

print('lcm of range:',min(li))
            
    
    
    

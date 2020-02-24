num=int(input('enter a no.:'))
temp=num
s=0
while(temp!=0):
        r=temp%10
        s+=r**3
        temp=(temp-r)/10
if(num==s):
        print(f'{num} is an armstrong number')
else:
        print("%d isn't an armstrong number"%num)

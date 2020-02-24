num=int(input('enter a no.:'))
temp=num
sum=0
while(temp!=0):
    remainder=temp%10
    sum+=remainder
    temp=(temp-remainder)/10
if(sum==num):
    print(f'{num} is a perfect number')
else:
    print(f"{num} isn't a perfect number")

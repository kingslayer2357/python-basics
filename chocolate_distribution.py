children=int(input('enter number of children:'))
choco=int(input('enter no. of chocolates:'))
li=children*[0]
while choco!=0:
    if choco>=children:
        n=choco//children
        r=choco%children
        for i in range(n):
            for n in range(len(li)):
                li[n]+=1
                choco-=1
        for j in range(r):
            li[j]+=1
            choco-=1
    else:
        r=choco
        for i in range(r):
            li[i]+=1
            choco-=1
print(li)

    

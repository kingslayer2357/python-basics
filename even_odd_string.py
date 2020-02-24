n=str(input('enter a string:'))
li=list(n)
even=''
odd=''
for k in range(len(li)):
    if (k+1)%2==0:
        even+=li[k]
    else:
        odd+=li[k]
print("even:",even ,"odd:",odd)

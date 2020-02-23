num=int(input('enter numerator:'))
den=int(input('enter denominator:'))
numli=[]
denli=[]
nli=[]
dli=[]
for i in range(1,num+1):
    if num%i==0:
        numli.append(i)
for j in range(1,den+1):
    if den%j==0:
        denli.append(j)
for n in numli:
    if n in denli:
        nli.append(n)
for d in denli:
    if d in numli:
        dli.append(d)
final_list=set(nli+dli)
m=max(final_list)
print('reduced fraction:')
print(int(num/m),'/',int(den/m))

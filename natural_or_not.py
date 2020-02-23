int_array=[]
n=int(input('enter no. of numbers:'))
for i in range(n):
    int_input=int(input('enter numbers:'))
    int_array.append(int_input)
x=True
for k in int_array:
    if k==0:
        x=False
    elif isinstance(k,float):
        x=False
    elif k<0:
        x=False
if x==True:
    print('entered numbers are all natural numbers')
else:
    print('not all entered are natural numbers')


"""find the no that constitute the reverse binary of the number entered by the user"""
num=int(input("Enter number:"))
b=bin(num)
br=b[2:]
bre=br[::-1]
new_num=0
for i in range(len(bre),0,-1):
    new_num+=int(bre[i-1])*(2**(len(bre)-i))
print(new_num)

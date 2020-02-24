p_li=[]
n=int(input('enter number of players:'))
for i in range(n):
    name=str(input('enter player name:'))
    p_li.append(name)
p_li=100*p_li
while len(set(p_li))!=1:
    die=p_li[1]
    p_li=[x for x in p_li if x!=die]
    p_li=p_li[1:]
print('winner:',p_li[0])
    

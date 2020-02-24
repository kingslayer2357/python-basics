print('''          FLAMES            ''')
name1=str(input("enter 1st person's name:"))
name2=str(input("enter 2nd person's name:"))
n1list=list(name1)
n2list=list(name2)
list1=[word1 for word1 in name1 if word1 in name2]
list2=[word2 for word2 in name2 if word2 in name1]
flist1=[word3 for word3 in n1list if word3 not in list1]
flist2=[word4 for word4 in n2list if word4 not in list2]
final_list=flist1+flist2
step=len(final_list)
flames_list=list(100*'flames')
x=True
while x:
    rem=flames_list[step-1]
    flames_list=flames_list[flames_list.index(rem):]
    flames_list=[word for word in flames_list if rem!=word]
    flames_set=set(flames_list)
    if len(flames_set)==1:
        x=False
li=list(flames_set)
dec=li[0]
def decider(dec):
    if dec=='f':
        print(f'{name1} and {name2} are friends.')
    elif dec=='l':
        print(f'{name1} and {name2} are in love.')
    elif dec=='a':
        print(f'{name1} and {name2} are having an affair.')
    elif dec=='m':
        print(f'{name1} and {name2} are destined to marry each other.')
    elif dec=='e':
        print(f'{name1} and {name2} are enemies.')
    else:
        print(f'{name1} and {name2} are to have sex.')
decider(dec)


    
    
    

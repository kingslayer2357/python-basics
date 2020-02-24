print('''       LOVE METER     ''')
def love():
 name1=str(input("enter 1st person's name:"))
 name2=str(input("enter 2nd person's name:"))
 love_str=name1+'love'+name2
 love_dic=dict()
 for word in love_str:
    if word in love_dic:
        love_dic[word]+=1
    else:
        love_dic[word]=1
 val_list=list(love_dic.values())
 while len(val_list)!=2:
    emp_list=[]
    while len(val_list)!=0 :
     if len(val_list)==1:
      emp_list.append(val_list[0])
      del val_list[0]
     else:
      s=val_list[0]+val_list[-1]
      emp_list.append(s)
      del val_list[0]
      del val_list[-1]
    val_list=emp_list
 percent=10*(val_list[1])+val_list[0]
 print(f'{name1} loves {name2} {percent}%')
love()

       


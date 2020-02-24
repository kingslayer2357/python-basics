import random
print('''         TIC,TAC,TOE       ''')
board_menu='''
              |   |
           _1_|_2_|_3_
              |   |
           _4_|_5_|_6_
              |   |
            7 | 8 | 9
                        '''
print(board_menu)
a,b,c,d,e,f,g,h,i=' ',' ',' ',' ',' ',' ',' ',' ',' '
position_list=['x','x','x','x','x','o','o','o','o','o']
#print(game_board)
player1=str(input('enter name of player 1:'))
player2=str(input('enter name of player 2:'))
print('''  TOSS TIME   ''')
toss=random.choice(['head','tail'])
player_list=[player1,player2]
toss_asker=random.choice(player_list)
player_list.remove(toss_asker)
if toss_asker==player1:
    print(f'{player1} will choose head or tail')
else:
    print(f'{player2} will choose head or tail')
toss_ask=str(input('choose one :( head or tail ):'))
if toss_ask==toss:
    print(f'{toss_asker} won the toss')
    toss_winner=toss_asker
    toss_loser=player_list[0]
else:
    print(f'{toss_asker} lost the toss')
    toss_winner=player_list[0]
    toss_loser=toss_asker
w_var=str(input(f'{toss_winner} choice: o or x :'))
if w_var=='x':
    l_var='o'
elif w_var=='o':
    l_var='x'
   

    
    
while len(position_list)!=1:
    if ((a,b,c)!=(w_var,w_var,w_var) and (c,f,i)!=(w_var,w_var,w_var) and (g,h,i)!=(w_var,w_var,w_var) and (a,d,g)!=(w_var,w_var,w_var) and (b,e,h)!=(w_var,w_var,w_var) and (c,e,g)!=(w_var,w_var,w_var) and (a,e,i)!=(w_var,w_var,w_var) and (d,e,f)!=(w_var,w_var,w_var)) and ((a,b,c)!=(l_var,l_var,l_var) and (c,f,i)!=(l_var,l_var,l_var) and (g,h,i)!=(l_var,l_var,l_var) and (a,d,g)!=(l_var,l_var,l_var) and (b,e,h)!=(l_var,l_var,l_var) and (c,e,g)!=(l_var,l_var,l_var) and (a,e,i)!=(l_var,l_var,l_var) and (d,e,f)!=(l_var,l_var,l_var)) :
        print(f"{toss_winner}'s turn:")
        position=int(input('enter a position:'))
        if position==1:
            a=w_var
            position_list.remove(w_var)
        elif position==2:
            b=w_var
            position_list.remove(w_var)
        elif position==3:
            c=w_var
            position_list.remove(w_var)
        elif position==4:
            d=w_var
            position_list.remove(w_var)
        elif position==5:
            e=w_var
            position_list.remove(w_var)
        elif position==6:
            f=w_var
            position_list.remove(w_var)
        elif position==7:
            g=w_var
            position_list.remove(w_var)
        elif position==8:
            h=w_var
            position_list.remove(w_var)
        elif position==9:
            i=w_var
            position_list.remove(w_var)
        
        else:
            print('invalid position')   
        print(f'''
          |   |
       _{ a }_|_{ b }_|_{ c }_
          |   |
       _{ d }_|_{ e }_|_{ f }_
          |   | 
        { g } | { h } | { i }   
                        ''') 
        if len(position_list)!=1 and ((a,b,c)!=(w_var,w_var,w_var) and (c,f,i)!=(w_var,w_var,w_var) and (g,h,i)!=(w_var,w_var,w_var) and (a,d,g)!=(w_var,w_var,w_var) and (b,e,h)!=(w_var,w_var,w_var) and (c,e,g)!=(w_var,w_var,w_var) and (a,e,i)!=(w_var,w_var,w_var) and (d,e,f)!=(w_var,w_var,w_var)) and ((a,b,c)!=(l_var,l_var,l_var) and (c,f,i)!=(l_var,l_var,l_var) and (g,h,i)!=(l_var,l_var,l_var) and (a,d,g)!=(l_var,l_var,l_var) and (b,e,h)!=(l_var,l_var,l_var) and (c,e,g)!=(l_var,l_var,l_var) and (a,e,i)!=(l_var,l_var,l_var) and (d,e,f)!=(l_var,l_var,l_var)):
            print(f"{toss_loser}'s turn:")
            position=int(input('enter a position:'))
            if position==1:
                a=l_var
                position_list.remove(l_var)
            elif position==2:
                b=l_var
                position_list.remove(l_var)
            elif position==3:
                c=l_var
                position_list.remove(l_var)
            elif position==4:
                d=l_var
                position_list.remove(l_var)
            elif position==5:
                e=l_var
                position_list.remove(l_var)
            elif position==6:
                f=l_var
                position_list.remove(l_var)
            elif position==7:
                g=l_var
                position_list.remove(l_var)
            elif position==8:
                h=l_var
                position_list.remove(l_var)
            elif position==9:
                i=l_var
                position_list.remove(l_var)
        
            else:
            
                print('invalid position')   
            print(f'''
          |   |
       _{ a }_|_{ b }_|_{ c }_
          |   |
       _{ d }_|_{ e }_|_{ f }_
          |   | 
        { g } | { h } | { i }   
                        ''')
    elif ((a,b,c)==(w_var,w_var,w_var) or (c,f,i)==(w_var,w_var,w_var) or (g,h,i)==(w_var,w_var,w_var) or (a,d,g)==(w_var,w_var,w_var) or (b,e,h)==(w_var,w_var,w_var) or (c,e,g)==(w_var,w_var,w_var) or (a,e,i)==(w_var,w_var,w_var) or (d,e,f)==(w_var,w_var,w_var)) :
            print(f'{toss_winner} win the game')
            break
    elif ((a,b,c)==(l_var,l_var,l_var) or (c,f,i)==(l_var,l_var,l_var) or (g,h,i)==(l_var,l_var,l_var) or (a,d,g)==(l_var,l_var,l_var) or (b,e,h)!=(l_var,l_var,l_var) or (c,e,g)!=(l_var,l_var,l_var) or (a,e,i)==(l_var,l_var,l_var) or (d,e,f)==(l_var,l_var,l_var)) :
            print(f'{toss_loser} win the game')
            break
else:
    print('game ends in a draw')

    
    
    

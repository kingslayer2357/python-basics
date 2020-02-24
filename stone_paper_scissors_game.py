import random
computer_options=['stone','paper','scissor']
win_quotes=['Well done!!','You did it!','You finally won','Sweet taste of victory!']
bigwin_quotes=['You are pro,man!','The champ is here','Take that Bitch!!']
loss_quotes=['Better luck next time','Try try but dont cry','dont give up!','I gotta feeling,you are one try away from victory']
bigloss_quotes=['You are a sore loser!','You need to man up,kid','noob!!!']
smallloss_quotes=['Damn that was close!','soooo close','AI barely survived!','for once i thought i won']
tie_quotes=['what a game!','luck got us','Once more!']
print('''     STONE,PAPER,SCISSOR     ''')
rounds=int(input('Enter number of rounds:'))
computer_score=0
human_score=0
for i in range(rounds):
    human_choice=str(input('Enter your choice:'))
    computer_choice=random.choice(computer_options)
    if (human_choice!='stone'and human_choice!='paper'and human_choice!='scissor'):
        print('Invalid choice')
        print('Pick one: stone,paper or scissor')
    elif (human_choice=='stone' and computer_choice=='stone'):
        print('IT IS A TIE')
        computer_score+=0
        human_score+=0
        print('computer score:',computer_score)
        print('human score:',human_score)
    elif(human_choice=='stone' and computer_choice=='paper'):
        print('COMPUTER WINS')
        computer_score+=1
        human_score+=0
        print('computer score:',computer_score)
        print('human score:',human_score)
    elif(human_choice=='stone' and computer_choice=='scissor'):
        print('YOU WIN')
        computer_score+=0
        human_score+=1
        print('computer score:',computer_score)
        print('human score:',human_score)
    elif(human_choice=='paper' and computer_choice=='stone'):
        print('YOU WIN')
        computer_score+=0
        human_score+=1
        print('computer score:',computer_score)
        print('human score:',human_score)
    elif(human_choice=='paper' and computer_choice=='paper'):
        print('IT IS A TIE')
        computer_score+=0
        human_score+=0
        print('computer score:',computer_score)
        print('human_scrore:',human_score)
    elif(human_choice=='paper' and computer_choice=='scissor'):
        print('COMPUTER WINS')
        computer_score+=1
        human_score+=0
        print('computer score:',computer_score)
        print('human score:',human_score)
    elif(human_choice=='scissor' and computer_choice=='stone'):
        print('COMPUTER WINS')
        computer_score+=1
        human_score+=0
        print('computer score:',computer_score)
        print('human score:',human_score)
    elif(human_choice=='scissor' and computer_choice=='paper'):
        print('YOU WIN')
        computer_score+=0
        human_score+=1
        print('computer score:',computer_score)
        print('human score:',human_score)
    elif(human_choice=='scissor' and computer_choice=='scissor'):
        print('IT IS A TIE')
        computer_score+=0
        human_score+=0
        print('computer score:',computer_score)
        print('human score:',human_score)
print('   Final Score:   ')
print('computer score:',computer_score)
print('human score:',human_score)
if(human_score>computer_score):
    print('   YOU WIN THE GAME   ')
    if(human_score-computer_score>4):
        msg=random.choice(bigwin_quotes)
        print('   ',msg,'   ')
    else:
        msg=random.choice(win_quotes)
        print('   ',msg,'   ')
if(computer_score>human_score):
    print('   YOU LOSE THE GAME   ')
    if(computer_score-human_score<=2):
        msg=random.choice(smallloss_quotes)
        print('   ',msg,'   ')
    elif(computer_score-human_score>4):
        msg=random.choice(bigloss_quotes)
        print('   ',msg,'   ')
    else:
        msg=random.choice(loss_quotes)
        print('   ',msg,'   ')
if(computer_score==human_score):
    print('   THE GAME ENDS IN A TIE   ')
    msg=random.choice(tie_quotes)
    print('   ',msg,'   ')


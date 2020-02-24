import sys
import random
class Cards():
    cards=[['Ace of Clubs',1],['Two of Clubs',2],['Three of Clubs',3],['Four of Clubs',4],['Five of Clubs',5],['Six of Clubs',6],['Seven of Clubs',7],['Eight of Clubs',8],['Nine of Clubs',9],['Ten of Clubs',10],['Jack of Clubs',10],['Queen of Clubs',10],['King of Clubs',10],['Ace of Spades',1],['Two of Spades',2],['Three of Spades',3],['Four of Spades',4],['Five of Spades',5],['Six of Spades',6],['Seven of Spades',7],['Eight of Spades',8],['Nine of Spades',9],['Ten of Spades',10],['Jack of Spades',10],['Queen of Spades',10],['King of Spades',10],['Ace of Hearts',1],['Two of Hearts',2],['Three of Hearts',3],['Four of Hearts',4],['Five of Hearts',5],['Six of Hearts',6],['Seven of Hearts',7],['Eight of Hearts',8],['Nine of Hearts',9],['Ten of Hearts',10],['Jack of Hearts',10],['Queen of Hearts',10],['King of Hearts',10],['Ace of Diamonds',1],['Two of Diamonds',2],['Three of Diamonds',3],['Four of Diamonds',4],['Five of Diamonds',5],['Six of Diamonds',6],['Seven of Diamonds',7],['Eight of Diamonds',8],['Nine of Diamonds',9],['Ten of Diamonds',10],['Jack of Diamonds',10],['Queen of Diamonds',10],['King of Diamonds',10]]
    def __init__(self):
        print('                  WELCOME TO BLACK JACK')
class HumanPlayer(Cards):
    def __init__(self,name):
        self.player_name=name.title()
        self.human_card_list=[]
        self.human_sum=0
        self.human_budget=10000
    def human_get_cards(self):
        for i in range(2):
                self.human_card=random.choice(self.cards)
                self.human_card_list.append(self.human_card[0])
                self.human_sum+=self.human_card[1]
                self.cards.remove(self.human_card)
        print(self.human_card_list)
    def human_hit(self):
        self.human_card=random.choice(self.cards)
        self.human_card_list.append(self.human_card[0])
        self.human_sum+=self.human_card[1]
        self.cards.remove(self.human_card)
        print(self.human_card_list)
    
    def human_stay(self):
        return self.human_sum
    def human_win_game(self):
        print(f'{self.player_name} win the game')
    def human_win_bet(self):
        print(f'{self.player_name} win the bet')
    def human_bet(self):
        print(f'Current Budget:{human.human_budget}')
        print('Minimum Bet:1000')
        while True:
            self.bet=int(input('Enter bet:'))
            if self.bet<=self.human_budget:
                break
            else:
                print(f'You have only ${self.human_budget} as your current budget') 
    def forfeit(self):
        print('You forfeited the game')
        print('Computer win the game')
        sys.exit()
class Computer(Cards):
    def __init__(self):
        self.comp_card_list=[]
        self.comp_sum=0
        self.comp_budget=10000
    def comp_get_cards(self):
        self.comp_card=random.choice(self.cards)
        self.comp_card_list.append(self.comp_card[0])
        self.comp_sum+=self.comp_card[1]
        self.cards.remove(self.comp_card)
        print(self.comp_card_list)
    def comp_hit(self):
        self.comp_card=random.choice(self.cards)
        self.comp_card_list.append(self.comp_card[0])
        self.comp_sum+=self.comp_card[1]
        self.cards.remove(self.comp_card)
        print(self.comp_card_list)
    def comp_stay(self):
        return self.comp_sum
    def comp_win_game(self):
        print('Computer win the game')
    def comp_win_bet(self):
        print('Computer win the bet')




        
card=Cards()
name=str(input('Enter your name:'))
human=HumanPlayer(name)
comp=Computer()
while human.human_budget!=0 and comp.comp_budget!=0:
    print("Computer's Cards:")
    comp.comp_get_cards()
    print(f"{human.player_name}'s Cards:")
    human.human_get_cards()
    human.human_bet()
    while human.human_sum<21:
        print('''
    1.Hit
    2.Stay
    3.Forfeit''')
        human_choice=int(input('Enter Choice:'))
        if human_choice==1:
            human.human_hit()
        elif human_choice==2:
            human.human_stay()
            while comp.comp_sum<21:
                comp.comp_hit()
                if comp.comp_sum<21:
                    if (21-comp.comp_sum)<(21-human.human_sum):
                        comp.comp_win_bet()
                        comp.comp_budget+=human.bet
                        human.human_budget-=human.bet
                        break
                
                elif comp.comp_sum==21:
                    comp.comp_win_bet()
                    comp.comp_budget+=human.bet
                    human.human_budget-=human.bet
                    break
                
                elif comp.comp_sum>21:
                    print('Computer Busts')
                    human.human_win_bet()
                    human.human_budget+=human.bet
                    comp.comp_budget-=human.bet
                    break
            break        
        elif human_choice==3:
            human.forfeit()
        else:
            print('Invalid Choice')
            sys.exit()
    if human.human_sum>21:
            print(f'{human.player_name} Busts')
            comp.comp_win_bet()
            comp.comp_budget+=human.bet
            human.human_budget-=human.bet
    elif human.human_sum==21:
        human.human_win_bet()
        human.human_budget+=human.bet
        comp.comp_budget-=human.bet
    human.human_card_list=[]
    comp.comp_card_list=[]
    human.human_sum=0
    comp.comp_sum=0
                
if human.human_budget==0:
    comp.comp_win_game()
elif comp.comp_budget==0:
    human.human_win_game()
    

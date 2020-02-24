import sys
import json
class AtmMachine(object):
    x=True
    atm_dict={
    'himanshu':[120000,'2357'],
    'kuchoo':[150000,'1432'],
    'papa':[200000,'1919'],
    'mummy':[170000,'0007'],
    'sam':[12000,'2222']
    }
    def __init__(self):
        print("      WELCOME TO ATM MACHINE  ")
    def login(self,name,pin):
        self.name=name
        self.pin=pin
        #with open('atm_dict.json','w') as fh:
             #json.dump(self.atm_dict,fh)
        with open('atm_dict.json') as fh:
             atm=json.load(fh)
        if self.name in atm:
            if atm[self.name][1]==self.pin:
                print(f'Welcome Mr./Ms.{self.name}')
            else:
                self.x=False
                print('Invalid name or pin')
                sys.exit()
        else:
            self.x=False
            print('Invalid name or pin')
            sys.exit() 
    def withdrawl(self,amount):
        self.amount=amount
        with open('atm_dict.json') as fh:
            atm=json.load(fh)
            if atm[self.name][0]>=self.amount:
                atm[self.name][0]-=self.amount
                with open('atm_dict.json','w') as fh:
                    json.dump(atm,fh)
                print(f'Updated Balance:{atm[self.name][0]}')
            else:
                print('You do not have enough money in your account')
                
                sys.exit()
    def deposit(self,amount):
        self.amount=amount
        with open('atm_dict.json') as fh:
            atm=json.load(fh)
            atm[self.name][0]+=self.amount
            with open('atm_dict.json','w') as fh:
                json.dump(atm,fh)
        print(f'Updated Balance:{atm[self.name][0]}')
    def check_bal(self):
        with open('atm_dict.json') as fh:
            atm=json.load(fh)
            print(f'Your Current Balance:{atm[self.name][0]}')
    def register(self,name,pin):
        self.name=name
        self.pin=pin
        with open('atm_dict.json') as fh:
            atm=json.load(fh)
            atm[self.name]=[0,self.pin]
        with open('atm_dict.json','w') as fh:
            json.dump(atm,fh)
            print(f'You Have Been Succesfully Registered {self.name}')
    def change_pin(self,new_pin):
        self.new_pin=new_pin
        with open('atm_dict.json') as fh:
            atm=json.load(fh)
            atm[self.name][1]=self.new_pin
            with open('atm_dict.json','w') as fh:
                json.dump(atm,fh)
                print('Pin Changed Successfully')
            
    def exit(self):
        sys.exit()

cc=AtmMachine()
print('''  LOG IN''')
name=str(input('Enter Name:'))
pin=str(input('Enter Pin:'))
cc.login(name,pin)

print('''
1.Withdraw Cash
2.Deposit Cash
3.Check Balance
4.Register
5.Change Pin
6.Exit
''')
choice=int(input('enter choice:'))
if choice==1:
    amount=int(input('Enter amount:'))
    cc.withdrawl(amount)
   
elif choice==2:
    amount=int(input('enter amount:'))
    cc.deposit(amount)
elif choice==3:
    cc.check_bal()
elif choice==4:
    name=str(input('Enter Name:'))
    pin=str(input('Enter Desired Pin:'))
    cc.register(name,pin)
elif choice==5:
    new_pin=str(input('Enter New Pin:'))
    cc.change_pin(new_pin)
elif choice==6:
    cc.exit()

import random
jumb_dict={
    'i saw a dog on my way home':'I saw a dog on my way home'.split(' '),
    'i am going to play in the park':'i am going to play in the park'.split(' '),
    'it is raining heavily' :'it is raining heavily'.split(' '),
    'i want to go home':'i want to go home'.split(' '),
    'i am a diehard fan of football':'i am a diehard fan of football'.split(' '),
    'i would rather have you executed': 'i would rather have you executed'.split(' '),
    'france won the 2018 edition of the world cup':'france won the 2018 edition of the world cup'.split(' '),
    'she used to work here but not any more':'she used to work here but not any more'.split(' '),
    'cristiano ronaldo is the best player in the world':'cristiano ronaldo is the best player in the world'.split(' '),
    'my father gifted me a new phone for my birthday':'my father gifted me a new phone for my birthday'.split(' '),
    'my mom cooks very delicious food':'my mom cooks very delicious food'.split(' '),
    'red wine is actually good for health':'red wine is actually good for health'.split(' '),
    'the taj mahal is loacted in agra':'the taj mahal is loacted in agra'.split(' '),
    'samarth is a complete joker': 'samarth is a complete joker'.split(' '),
    'my favourite movie is the dark knight':'my favourite movie is the dark knight'.split(' ')
    }
print('''     JUMBLED SENTENCES     ''')
score=0
jumb_list=[]
for key,value in jumb_dict.items():
    jumb_list.append(value)
for k in range(15):
    ran_select=random.choice(jumb_list)
    jumb_list.remove(ran_select)
    random.shuffle(ran_select)
    print('ques %d:'%(k+1),ran_select)
    ans=str(input('Arranged Sentence:'))
    if ans in jumb_dict:
        score+=1
    else:
        score+=0
print('score:',score,"out of 15")

        

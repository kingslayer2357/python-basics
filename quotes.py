quote=str(input('enter a quote:'))
q_list=quote.split(' ')
li=[]
for word in q_list:
    word=word[0].upper()+word[1:]
    li.append(word)
print(' '.join(li))


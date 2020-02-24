s=str(input('write a sentence:'))
s_li=s.split(' ')
for k in s_li:
    s_li.sort(key=lambda val:len(val),reverse=True)
print('longest word:',s_li[0])

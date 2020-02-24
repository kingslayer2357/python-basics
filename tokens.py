import re
s=input('enter character:')
if re.search('[0-9]',s):
    print(f'{s} is integer')
    if re.search('[a-b]',s):
        print(f'{s} is a variable')
elif isinstance(s,str):
    print(f'{s} is string')

import re
print('Your pasword should be 6 to 12 character long,contain atleast one uppercase one lower case and atleast one numerical character')
password=input('enter password:')
x=True
while x:
    if len(password)<6 or len(password)>12:
        break
    elif not re.search('[A-Z]',password):
        break
    elif not re.search('[a-z]',password):
        break
    elif re.search('[0-9]',password):
        x=False
        print('valid password')
        break
if x==True:
    print('invalid password')
    

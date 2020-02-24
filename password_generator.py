import random
import re
def password_generator():
 p_len_list=list(range(6,17))
 p_len=random.choice(p_len_list)
 p_char_list=['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*',"Q","W","E","R",'T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
 p_list=[]
 for i in range(p_len):
    p_char=random.choice(p_char_list)
    p_list.append(p_char)
 password=(''.join(p_list))
 x=True
 while x!=False:
     if not re.search('[a-z]',password):
         break
     if not re.search('[A-Z]',password):
         break
     if not re.search('[0-9]',password):
         break
     if re.search('[!@#$%^&*]',password):
         print(password)
         x=False
         break
 if x==False:
     print(password)
 
    
print('Your password:')
password_generator()


 
    
    

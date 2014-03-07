# '''
# Created on Feb 27, 2014
# 
# @author: anshulchawla
# '''
# 
# import re
# 
# # . (dot ) matches any character except new line one characher per dot.
# # does left to right so takes the first one from the left
# match = re.search('...n','Its a cool world anshulanshul')
# if match:
#   print(match.group())
# # /w word char a-z 0-9 etc but no punctuation or special character or space
# # /d digit 
# # /s white space
# # /S is opposite or whit space, it means except white space
# # + one or more
# # * zero or more
# # put * or + after the charater for appropriate match
# # [] order inside bracket does not matter [\w.] is same as [.\w]
# # () with saparate items in group as separate. ()+ doesnot mean multiple arrayitems
# match= re.search('ansi', 'Its a cool worldanshul')
# if match:
#   print(match.group())
# else:
#   print('Not Found') 
#   
# match= re.search('(\d+\s*)+','1 2 3')
# if match:
#   print(match.group())
# else:
#   print('not found')     
#   
# match=re.search('([\w*\.]+)@(\w+)\.(\w+)','ansjdhsj asf%anshul.ankush@yahoo.com%s anshulankush@gmail.com')  
# if match:
#   print(match.group(0))
# else:
#   print('not found')     
#   
# match=re.findall('([\w*\.]+)@(\w+)\.(\w+)','ansjdhsj asf%anshul.ankush@yahoo.com%s anshulankush@gmail.com')  
# if match:
#   print(match)
# else:
#   print('not found')       
#   
# import shutil
# 
# shutil.copy('BasicOperations.py', '/Users/anshulchawla/Desktop')  
# 
# 
# 
# 
d={}
i=0  

while True:
  try:
    d[str(i)+'dfhaskdfhadjkfhdkjfhaskfhaslhfajshfaksdhfakshfkfhakjfhaskjdfhsdkjfhaskjdfhajkfhasdjfhakjdfhadskjfhasdkjfhaskdjhf'] = True
    i+=1
    if i%1000000==0:
      print('i: '+str(i))
  except Exception:
    print(i)    
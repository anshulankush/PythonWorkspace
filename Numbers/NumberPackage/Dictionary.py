'''
Created on Feb 26, 2014

@author: anshulchawla
'''
D={}
D['a'] = 'alpha'
D['o'] = 'omega'
D['g'] = 'gamma'

# print(D['A'])


# Better way!
print(D.get('A'))

print('a' in D)

print(D.keys())#Random Order
print(D.values())

for k in sorted(D.keys()):
  print('KEY: {}, VALUE: {}'.format(k, D.get(k)))
  
print(D.items())  

for k in sorted(D.items()):
  print('KEY: {}'.format(k))
  
  
x=1
y=1
n=3
m=3
# count=0

def count_path(x, y):
  c=0
  if(x==n) and (y==m):
#     count+=1
    return 1  
    
  if x<n:
    c+=count_path(x+1, y)
  
  if y<m:
    c+=count_path(x, y+1)
  
  
  return c  
    
    

x=count_path(x, y)
print(x)
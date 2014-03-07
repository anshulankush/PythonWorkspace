from Point import Point
from Queue import Queue
class Main:
  p = Point()
  D = {}
  q = Queue()
  count=0
  
  if p.validate(D):
    q.put(p)
    count+=1
  
  while not q.empty():
    p = q.get()

    x = p.get_x()
    y = p.get_y()
    
    left = Point(x-1,y)
    if left.validate(D):
      q.put(left)
      count+=1
      
      
    right = Point(x+1,y)
    if right.validate(D):
      q.put(right)
      count+=1
   
    top = Point(x,y+1)
    if top.validate(D):
      q.put(top)
      count+=1
    
    bottom = Point(x,y-1)
    if bottom.validate(D):
      q.put(bottom)
      count+=1
    
 
  print(count)
  
    
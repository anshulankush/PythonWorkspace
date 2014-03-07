class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  
  def get_string(self):
    return str(self.x) + ',' + str(self.y)
  
  def summation(self,a):
    a = abs(a)
    sm = 0
    while(a > 0):
      sm += a % 10
      a = a / 10
    return sm
      
  def validate(self,D):
    a = self.x
    b = self.y
    p = Point(a,b)
    if ( p.get_string() in D)  is True:
      return False
    final_sum = (p.summation(a) + p.summation(b))
    if final_sum<=19:
      D[str(a) +','+ str(b)] = True
    return final_sum<=19
    
  def get_x(self):
    return self.x
  
  def get_y(self):
    return self.y
  
    
    
    
    
    
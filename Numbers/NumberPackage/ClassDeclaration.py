class parentClass1:
  var1="tushar"
  var4=30
  
class parentClass2:
  var1="anshul"
    
class child(parentClass2, parentClass1):
  pass
   
c=child()
print(c.var1)
print(c.var4)            
   
   
class childClass(parentClass1):
    pass # dont do anything
 
parentObject=parentClass1()
print(parentObject.var1)
 
childObject= childClass()
print(childObject.var2)
         
class child1(parentClass1):
    var2=1        
         
c=child()
print(c.var1)
print(c.var2)
print(parentObject.var1)
print(parentObject.var2)        
# myObject=myClass()
# print(myObject.var1)      
# print(myObject.var2)
# myObject.myFunction("Dude!!!") 
 
#self is a temporary placeholder for the object itself
 
class class1:
    def createMethod(self,name):
        self.name=name;
         
    def myMethod(self):
        print("Hello {}".format(self.name))
              
o=class1()
o.createMethod("Tushar!!!")
 
a=class1()
a.createMethod("temp")  
o.myMethod()
a.myMethod()
print(o.name)
print(a.name)
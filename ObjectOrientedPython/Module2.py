# class pet:
#   number_of_legs = 0
#   
#   def sleep(self):
#     print('zzz')
#   
# #   def count_legs(self):
# #     print('legs from variable in own class: {}' .format(pet_object.number_of_legs))
# #   
#   def count_legs_with_self(self):
#     print('legs from variable in own class: {}' .format(self.number_of_legs))
from Module1 import pet
 
class dog(pet):
  def bark(self):
    print('Woof')
    
dog_object = dog()
dog_object.bark()
dog_object.sleep()
dog_object.number_of_legs=9
dog_object.count_legs_with_self()    
class pet:
  number_of_legs = 0
  
  def sleep(self):
    print('zzz')
  
#   def count_legs(self):
#     print('legs from variable in own class: {}' .format(pet_object.number_of_legs))
#   
  def count_legs_with_self(self):
    print('legs from variable in own class: {}' .format(self.number_of_legs))
  
# pet_object = pet()
# pet_object.number_of_legs = 4
# 
# print('pet has {} legs'.format(pet_object.number_of_legs))
# # calling method in class pet   
# pet_object.sleep()
# pet_object.count_legs()
# 
# fish_object = pet()
# fish_object.count_legs()
# print('')
# pet_object.count_legs_with_self()
# fish_object.count_legs_with_self()

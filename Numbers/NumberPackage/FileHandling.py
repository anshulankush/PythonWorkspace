#fixes dos and unix endings under the hood
fob=open('/Users/anshulchawla/Documents/PythonWorkspace/GoogleDeveloper/small.txt','rU')
# for line in fob:
#  #put comma in end to remove line doubling
#   print(line),
line=fob.readlines()
# print(line)

text=fob.read()
print(1)
print(text),
print(2)
fob.close()




 






# 
# fob=open('/Users/anshulchawla/Desktop/a.txt','w')
# fob.write("hello text file")
# fob.write("\nhello text file1")
# fob.write("\nhello text file2")
# fob.write("\nhello text file3")
# fob.write("\nhello text file4")
#  
# fob.close()
#  
# fob=open("/Users/anshulchawla/Desktop/a.txt","r")
# listMe=fob.readlines()
# print(listMe)
# listMe[0]="Updated list\n"
# fob.close()
# fob=open("/Users/anshulchawla/Desktop/a.txt","w")
#  
# fob.writelines(listMe)
# fob.close()
# fob=open("/Users/anshulchawla/Desktop/a.txt","r")
#  
# listMe=fob.readlines()
# print(listMe)

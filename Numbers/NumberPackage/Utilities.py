import os
import commands
import sys
import shutil
from zipfile import ZipFile


def directory_path(dire):
  filenames= os.listdir(dire)
  for filename in filenames:
#     print(os.path.join(filename))
#     print("absolute "+ os.path.abspath(filename))
    comand= 'ls -l ' + dire
    (status,output)= commands.getstatusoutput(comand)
    if status:
      sys.stderr( 'there was an error:', output)
      sys.exit(1) 

directory_path('/Users/anshulchawla/Desktop/')


# print(os.path.exists('/Users/anshulchawla/Desktop/Simple-KML1'))

# os.mkdir('/Users/anshulchawla/Desktop/VisaFolderTest')

shutil.copy('BasicOperations.py', '/Users/anshulchawla/Desktop')  


zf = ZipFile('/Users/anshulchawla/Documents/PythonWorkspace/GoogleDeveloper/Day2/newDir.zip','w')
zf.write('/Users/anshulchawla/Documents/PythonWorkspace/GoogleDeveloper/Day2/newDir')
zf.close()
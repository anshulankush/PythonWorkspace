#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
from zipfile import ZipFile

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them



def main():
  filenames=os.listdir('.')
#   print(filename)
  try:
    for filename in filenames:
      match = re.search('.*__.*__.*',filename)
      if match:
#         print(os.path.abspath(match.group()))
#         print os.path.exists('../newDir')
        if os.path.exists('.../newDir') == False:
          os.mkdir('.../newDir')   
          
        print (os.path.abspath('.../newDir'))
        shutil.copy(match.group(),'.../newDir')
     
    zf = ZipFile('.../newDir.zip','w')
    zf.write('.../newDir')
    zf.close()
  except Exception as e:
    print('Error:   '+ `e`)
    
      


if __name__ == "__main__":
  main()

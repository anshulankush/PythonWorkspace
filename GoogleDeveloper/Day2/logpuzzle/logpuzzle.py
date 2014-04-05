#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
from urllib import urlretrieve

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  f = open(filename)
  
  text = f.readlines()
  host = 'http://code.google.com'
  d={}
  for line in text:
    match = re.search('GET (/edu/\S*.jpg)', line)
    if match:
#       print(host+match.group(1))
      d[host+match.group(1)]=1
#     else:
#       print('not found')
  i=0;   
  image_list=[]
  for k in sorted(d.keys()):
    print(k)
    image_list.append(k)
  return image_list  

def download_images(img_urls, dest_dir):
  i=0;
  for url in img_urls:
    try:
      urlretrieve(url, './Images/image'+`i`+'.jpg')
    except Exception as e:
      print('Error: '+e) 
    i+=1


def display_image():
  fob = open('./Images/index.html','w')
  fob.write('<html><body>')
  for i in range(0,20):
    fob.write("<img src=\"image"+`i`+".jpg\">")
     
  fob.write('</body></html>')
   
#   pass

def main():
  filename = 'animal_code.google.com'
#   = './place_code.google.com'
#   image_urls = read_urls(filename)
#   download_images(image_urls, './images')
  display_image()
  
if __name__ == '__main__':
  main()

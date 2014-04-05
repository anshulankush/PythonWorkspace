from urllib2 import Request, urlopen, URLError
from urllib import urlretrieve
request = Request('http://google.com')

i=0

try:
  response = urlopen(request)
  kittens = response.read()
#     print(len(kittens))
#     if i==3:
#       print (kittens[:])
#       print('\n\n\n==============================================================================================================\n\n\n')
#     if i%10==0:
  print(kittens)
  i+=1
#   except:
#     print('Erroe!!!!!')
#   i+=1
except Exception as e:
    print ('Got an error code:', e)

urlretrieve('http://google.com/images/google_favicon_128.png','/Users/anshulchawla/Desktop/test_file_download.png')


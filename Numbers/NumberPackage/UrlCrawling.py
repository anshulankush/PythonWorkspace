from urllib2 import Request, urlopen, URLError
request = Request('https://stream.twitter.com/1/statuses/sample.json')

i=0
while True:
  try:
    response = urlopen(request)
    kittens = response.read()
#     print(len(kittens))
#     if i==3:
#       print (kittens[:])
#       print('\n\n\n==============================================================================================================\n\n\n')
#     if i%10==0:
    print(i)
    i+=1
#   except:
#     print('Erroe!!!!!')
#   i+=1
  except Exception as e:
      print ('Got an error code:', e)
      break; 
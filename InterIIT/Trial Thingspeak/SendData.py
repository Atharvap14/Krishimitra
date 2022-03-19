import sys
from time import sleep
import urllib3

a = 0
b = 1
c = 0
baseURL = 'https://api.thingspeak.com/update?api_key=2YN2MCB3402ONTMQ&field1='
http = urllib3.PoolManager()
response = http.request('GET', baseURL+'10')
print(response)
print ("Program has ended")

import json
import pandas as pd
import urllib3

a = 0
b = 1
c = 0
baseURL = 'https://api.thingspeak.com/channels/1677274/fields/1.json?api_key=IM12G9K17XCZT79G&results=60'
http = urllib3.PoolManager()
response = http.request('GET', baseURL)
data = json.loads(response.data)
Inference_DF = pd.read_json(data['feeds'])
print(Inference_DF)




    
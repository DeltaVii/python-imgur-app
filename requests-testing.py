#This is a testing file meant to help me understand Requests better

import requests

#r for request
#URLs are strings
#r = requests.get('https://github.com/timeline.json')

#Getting any text from the url

#print(r.text)

#Getting JSON data from the url

#print(r.json)

#Getting Header data from url

#print("\n\n",r.headers)
#Two ways of getting the same info from the headers dictionary
#print("\n",r.headers["Content-Type"])
#print(r.headers.get('content-type'))

#variable of headers
#resp = requests.head("http://google.com")
#print(resp.status_code,resp.text,resp.headers)

client_id = '16bb853579ca0a9'
params = {"client_id" : client_id}
r = requests.get("https://api.imgur.com/3/account/DeltaViii", data=params)
print(r)
j = r.json
print(j)

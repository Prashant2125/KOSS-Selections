import requests
import json
import time

start = time.time()

for i in range(1, 201):
    r = requests.get(f'https://xkcd.com/{i}/info.0.json')
    package = r.json()
    package_string=json.dumps(package,indent = 2)
    f=open("jsonurlstorage.txt","a")
    f.write(package_string)
    
time_taken = time.time() - start
print(f"time taken is {time_taken}")
#the time taken was 93.7406759262085s
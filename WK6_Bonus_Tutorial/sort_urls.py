import requests
import sys

URL = sys.argv[1]

response = requests.get(URL)
data = response.text
lines = data.split('\n')

url_count = {}
for line in lines:
    try:
        url = line.split(' ')[6]
        if url not in url_count:
            url_count[url] = 0
        url_count[url] += 1
    except:
        pass
        
sorted_url_count = sorted(url_count.items(), key=lambda x: x[1], reverse=True)
print(sorted_url_count[:10])

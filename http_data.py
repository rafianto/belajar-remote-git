import json
from urllib import request

# tentukan url endpoint
url = "https://api.github.com/users/rafianto"

# lakukan http request ke server
response = request.urlopen(url)

# parsing data json
data = json.loads(response.read())

# cetak hasil parsing data
print(data)
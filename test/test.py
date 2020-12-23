import urllib.request

response = urllib.request.urlopen("http://httpbin.org/get")
print(response.read().decode("utf-8"))
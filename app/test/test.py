import requests

response=requests.post("http://192.168.31.3:5000/predict")
print(response.text)
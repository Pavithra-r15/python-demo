import requests
import os

def request():

 try:
     try: 
      api = os.environ ['api-key']
      print("API Key found", api)
     except:
      api = os.environ("api-key1")
      print("error")
     else:
      url= f"http://api.weatherapi.com/v1/current.json?key={api}&q=trichy"
      response = requests.get(url)
      data= response.json()
      print(data)
 except Exception as error:
    print('Error', error) 

request()
import requests

api_key = '74d66f3d8fe5980c6bdd3deb97fb1783'

#get input from user
city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

#get info from url
response = requests.get(url)

#main code
if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    celsius = temp - 273
    print(f'Temperature: {celsius} C')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')
 

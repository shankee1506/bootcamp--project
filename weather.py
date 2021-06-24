import requests
#import os
from datetime import datetime

api_key = '8f75fe941670c44e2fbace72a83667c7'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

report = open('weather_info.txt','w')
report.write ("-------------------------------------------------------------"+"\n")
report.write ("Weather Stats for - {}  || {}".format(location.upper(), date_time)+"\n")
report.write ("-------------------------------------------------------------"+"\n")

report.write ("Current temperature is: {:.2f} deg C".format(temp_city)+"\n")
report.write ("Current weather desc  :"+weather_desc+"\n")
report.write ("Current Humidity      :"+str(hmdt)+ '%'+"\n")
report.write ("Current wind speed    :"+str(wind_spd) +'kmph'+"\n")

report.close()
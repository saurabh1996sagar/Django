from django.shortcuts import render
import urllib
import json


def index(request):
    return render(request,'index.html')

def result(request):
    if request.method == 'POST' :
        city = request.POST['city']

        source = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + city +"&units=metric&appid=91def13939672ddf7159ec1b91ae5766 ").read()

        data = json.loads(source)

        print(data)
        context = {
            'city_name' : city,
            'country_code' :str(data["sys"]["country"]),
            'coords' : "Lat : " + str(data["coord"]["lat"]) + " |Lon : "  + str(data["coord"]["lon"]),   
            'main' :str(data["weather"][0]["main"]),
            'description' : str(data["weather"][0]["description"]),
            'temperature' : str(data["main"]["temp"]),
            'pressure' : str(data["main"]["pressure"]),
            'humidity' : str(data["main"]["humidity"])
        }
        return render (request,'result.html',context)
    else:
        return render(request,'result.html')    

              
        




#         {
#   "coord": {
#     "lon": -122.08,
#     "lat": 37.39
#   },
#   "weather": [
#     {
#       "id": 800,
#       "main": "Clear",
#       "description": "clear sky",
#       "icon": "01d"
#     }
#   ],
#   "base": "stations",
#   "main": {
#     "temp": 282.55,
#     "feels_like": 281.86,
#     "temp_min": 280.37,
#     "temp_max": 284.26,
#     "pressure": 1023,
#     "humidity": 100
#   },
#   "visibility": 10000,
#   "wind": {
#     "speed": 1.5,
#     "deg": 350
#   },
#   "clouds": {
#     "all": 1
#   },
#   "dt": 1560350645,
#   "sys": {
#     "type": 1,
#     "id": 5122,
#     "message": 0.0139,
#     "country": "US",
#     "sunrise": 1560343627,
#     "sunset": 1560396563
#   },
#   "timezone": -25200,
#   "id": 420006353,
#   "name": "Mountain View",
#   "cod": 200
#   }                         

                        





















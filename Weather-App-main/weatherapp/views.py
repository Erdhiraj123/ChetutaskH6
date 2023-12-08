from django.shortcuts import render
from django.views import View
import requests
import datetime


#******************************** Class Based Views ******************************************

class Home(View):

    template = 'weatherapp/index.html'

    def get_city(self, request, *args, **kwargs):
        if request.method == 'POST':
            return request.POST.get('city', 'patna')
        return 'patna'
 

    def get_weather(self, city, *args, **kwargs):
        weather_api_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=b0d85f0cd81af373d3a89c274d795423'
        openweathermap_url = weather_api_url.format(city)

        try:
            openweathermap_data = requests.get(openweathermap_url, params={'units': 'metric'}).json()
            description = openweathermap_data['weather'][0]['description']
            icon = openweathermap_data['weather'][0]['icon']
            temp = openweathermap_data['main']['temp']
            day = datetime.date.today()

            return {
                'description': description,
                'icon': icon,
                'temp': temp,
                'day': day,
                'city': city,
                'exception_occurred': False,
            }

        except KeyError:
            exception_occurred = True
            day = datetime.date.today()
            return {
                'description': 'clear sky',
                'icon': '01d',
                'temp': 25,
                'day': day,
                'city': 'patna',
                'exception_occurred': exception_occurred,
            }
    
    def post(self, request, *args, **kwargs):
        city = self.get_city(request)
        weather_data = self.get_weather(city)
        return render(request, self.template, weather_data)

    def get(self, request, *args, **kwargs):
        city = self.get_city(request)
        weather_data = self.get_weather(city)
        return render(request, self.template, weather_data)


#******************************** Function Based Views ******************************************


# from django.shortcuts import render
# from django.contrib import messages
# import requests
# import datetime

# def home(request):
#     if 'city' in request.POST:
#         city = request.POST['city']
#     else:
#         city = 'patna'

#     # OpenWeatherMap API
#     weather_api_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=b0d85f0cd81af373d3a89c274d795423'
#     openweathermap_url = weather_api_url.format(city)


#     try:
#         # Get data from OpenWeatherMap API
#         openweathermap_data = requests.get(openweathermap_url, params={'units': 'metric'}).json()
#         description = openweathermap_data['weather'][0]['description']
#         icon = openweathermap_data['weather'][0]['icon']
#         temp = openweathermap_data['main']['temp']
#         day = datetime.date.today()

#         return render(request, 'weatherapp/index.html', {
#             'description': description,
#             'icon': icon,
#             'temp': temp,
#             'day': day,
#             'city': city,
#             'exception_occurred': False,
          
#         })

#     except KeyError as e:
#         exception_occurred = True
#         day = datetime.date.today()

#         return render(request, 'weatherapp/index.html', {
#             'description': 'clear sky',
#             'icon': '01d',
#             'temp': 25,
#             'day': day,
#             'city': 'patna',
#             'exception_occurred': exception_occurred,
            
#         })


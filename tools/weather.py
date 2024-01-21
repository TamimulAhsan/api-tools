import os
import sys
import datetime
import requests
from tools import menu
from api import api


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def weather():

    #The fancy One
    def weather_fancy(city):
        clear_screen()
        url = 'https://wttr.in/{}'.format(city)
        data = requests.get(url)
        result = data.text
        print(result)


    # The simple yet complicated one
    def weather_simple(city):
        clear_screen()
        api_key = api.get_api_key("openweathermap")

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            # Format the Json Data
            city = data['name']

            #convert unix time to H:M:S
            unix_time = data['dt']
            date_time_obj = datetime.datetime.fromtimestamp(unix_time)
            time = date_time_obj.strftime("%H:%M:%S")
            unix_sunrise = data['sys']['sunrise']
            sunrise_obj = datetime.datetime.fromtimestamp(unix_sunrise)
            sunrise = sunrise_obj.strftime("%H:%M:%S")
            unix_sunset = data['sys']['sunset']
            sunset_obj = datetime.datetime.fromtimestamp(unix_sunset)
            sunset = sunset_obj.strftime("%H:%M:%S")

            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            clouds = data['clouds']['all']
            temp_min = data['main']['temp_min']
            temp_max = data['main']['temp_max']
            visibility = data['visibility']
            wind_speed = data['wind']['speed']
            country = data['sys']['country']
            timezone = data['timezone']
            humidity = data['main']['humidity']
            latitude = data['coord']['lat']
            longitude = data['coord']['lon']


            print("\n\n=========================================")
            print("             Weather Information              ")
            print("                          --by Tamimul Ahsan")
            print("============================================\n")
            print(f"Time       :\t{time}")
            print(f"Temparature:\t{temp} ℃")
            print(f"Feels Like :\t{feels_like} ℃")
            print(f"Minimum    :\t{temp_min} ℃")
            print(f"Maximum    :\t{temp_max} ℃\n\n")
            print("============================================")
            print("              Location INFO                 ")
            print("============================================\n")
            print(f"City       :\t{city}")
            print(f"Country    :\t{country}")
            print(f"Timezone   :\t{timezone}")
            print(f"Latitude   :\t{latitude}")
            print(f"Longitude  :\t{longitude}\n\n")
            print("============================================")
            print("              Other Information             ")
            print("============================================\n")
            print(f"Sunrise    :\t{sunrise}")
            print(f"Sunset     :\t{sunset}")
            print(f"Humidity   :\t{humidity}%")
            print(f"Cloud      :\t{clouds}")
            print(f"Wind Speed :\t{wind_speed} Km/h")
            print(f"Visibility :\t{visibility}")


            input("\n\nPress Enter key to continue...")
            clear_screen()
        else:
            print(f"Something went wrong. Error Code: {response.status_code}\n\n")


    clear_screen()
    while 1:
        print("Select desired Method...\n")
        weather_selection = input("1. Regular\t2. Fancy\n3. Main Menu\t0. Exit\n > ")
        if weather_selection == '1':
            weather_simple(input("\nCity: "))
        elif weather_selection == '2':
            weather_fancy(input("\nCity: "))
        elif weather_selection == '3':
            menu.main()
        elif weather_selection == '0':
            sys.exit()
        else:
            print("Invalid Selection.")

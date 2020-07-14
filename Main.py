# import required modules
import requests
import PySimpleGUI as sg

# Enter your API key here
api_key = "2c90ea371cc5b1fa55fbfdb455130fcb"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = input("Enter city name : ")

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()


# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":
    a = x["weather"]
    a = a[0]
    iconnum = a['icon']

    # store the value of "main"
    # key in variable y
    print(x)
    y = x["main"]

    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
    current_temperature = round((current_temperature-273), 1)

    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]

    # store the value corresponding
    # to the "humidity" key of y
    current_humidiy = y["humidity"]

    # store the value of "weather"
    # key in variable z
    z = x["weather"]
    Main_description = z[0]
    Main_description = Main_description['main']
    print(Main_description)

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    # print following values
    print(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage) = " +
          str(current_humidiy) +
          "\n description = " +
          str(weather_description))

else:
    print(" City Not Found ")

#Rain
if Main_description == 'Rain':
    Pic = "Rain.png"
#Thunderstorm
elif Main_description == 'Thunderstorm':
    Pic = "Thunderstorm.png"
#Drizzle
elif Main_description == 'Drizzle':
    Pic = "SunnyRain.png"
#Clouds
elif Main_description == 'Clouds':
    Pic = "Clouds.png"
#Snow
elif Main_description == 'Snow':
    Pic = "Snow.png"
#Clear
elif Main_description == 'Clear':
    Pic = "Clear.png"
#If none else
else:
    Pic = "NA.png"


sg.theme('DarkBlue')

weather_description = weather_description.title()

# STEP 1 define the layout
layout = [
            [sg.Image(r'C:\Users\Benjy\Desktop\Code\~Python\Weather app\Picture\\' + Pic), ],
            [sg.Text((weather_description), font=("Helvetica", 30))],
            [sg.Text("Temperature:     " + str(current_temperature) + "°C")],
            [sg.Text("Humidity (%):    " + str(current_humidiy))],
            [sg.Text("Pressure (hPa):  " + str(current_pressure))],
            [sg.Button('X')]
         ]

#STEP 2 - create the window
window = sg.Window('WEATHER APP', layout, size=(400,300), grab_anywhere=True, no_titlebar=True)

# STEP3 - the event loop
while True:
    event, values = window.read()   # Read the event that happened and the values dictionary
    print(event, values)
    if event == 'X':     # If user closed window with X or if user clicked "Exit" button then exit
        break
window.close()
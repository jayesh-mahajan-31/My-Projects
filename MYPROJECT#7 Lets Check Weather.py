import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("Choose the city you want to know weather")
    city=input("City: ")
    url=f"http://api.weatherapi.com/v1/current.json?key=76f12697137b4ee980f141930221010&q={city}&aqi=no"
    wtr=requests.get(url).text
    wtr_dict=json.loads(wtr)
    try:
        data=wtr_dict["current"]["condition"]["text"]
        
    except Exception:
        speak("Please Enter correct name of the city")
    speak(f"Today's Weather in {city}")
    speak(data)
    print(data.upper())
    speak("For more details click on the link shown:")
    print("https://www.accuweather.com/en/in/pune/204848/weather-forecast/204848")
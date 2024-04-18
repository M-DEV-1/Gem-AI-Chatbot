

import requests

def temp_city(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather" #endpoint
    querystring = {"location":city,"format":"json","u":"f"}
    headers = {
	"X-RapidAPI-Key": "9d2319d7damshb2d0b4b87da2a7ap1d31d9jsnb8ab903af7be",
	"X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
 }
    response = requests.get(url, headers=headers, params=querystring)
    
    d1 = response.json()
    #print (d1)
    d1 = d1.get("current_observation")
    hum = d1.get('atmosphere').get("humidity")
    temp = d1.get('condition').get("temperature")
    temp = round((temp-32)*5/9,2)
    return (f"Humidity: {hum}, Temp in C: {temp}")
    #print(response.json())
    
if __name__ == "__main__": #Sumit is called Sumit but he calls himself, I or we
    #we call the program by its name
    #but it calls itself __main__ (__name__)
    #when it is imported, its name is not __main__
    print(temp_city("Delhi"))
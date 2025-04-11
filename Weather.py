from dotenv import load_dotenv
import requests
import os

load_dotenv()

def get_weather(user_input):

    try:
        #api_url = "https://jsonplaceholder.typicode.com/todos"
    # todo = {"userId": 2, "title": "Buy eggs", "completed": False}
        #response = requests.post(api_url, json=todo)
        #print(response.json())


        #print(response.status_code)

        #api_url = "https://jsonplaceholder.typicode.com/todos/2"
        #response = requests.get(api_url)
        #response.json()
        #print("STATUS CODE", response.status_code)
        #print("STAT", response.json())


     


        api_url_weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={os.getenv('api_key')}&units=metric")
        if api_url_weather.json()['cod'] == '404':
        #    print("No city found or incorrect city entered, Please try again")
            print(api_url_weather.json())
            status_code = api_url_weather.json()
            print(status_code)
            return status_code
        else:
            weather_data = api_url_weather.json()
            #Main_weather = api_url_weather.json()["weather"][0]["main"]
            #weather_desc = api_url_weather.json()["weather"][0]["description"]
            #temp = round(api_url_weather.json()["main"]["temp"])
            #Feels_like = round(api_url_weather.json()["main"]["feels_like"])

            #print(f"The weather forcast in {user_input} is {Main_weather} with {weather_desc}. The temperature is {temp}°C but it feels like {Feels_like}°C")
            return weather_data
    except Exception as e:
        print("No internet connection, please check your internet connection and try again")
        print(f"An error has occured {e}")


if __name__ == '__main__':
    user_input = input("Enter a city: ")
    get_weather(user_input)

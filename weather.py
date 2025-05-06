import requests

def get_weather(city):
    api_key = "https://wttr.in/{}?format=3".format(city)
    try:
        response = requests.get(api_key)
        if response.status_code == 200:
            print(response.text)
        else:
            print("Failed to retrieve weather data.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    print("Simple Terminal Weather Checker 🌦")
    city = input("Enter city name: ")
    get_weather(city)

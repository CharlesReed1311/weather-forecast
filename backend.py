import requests

API_KEY = "18c7307e66797ee57ecbdc83901c9013"

def get_data(place, forecast_days, kind):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data =  response.json()
    filtered_data = data["list"]
    no_of_values = 8*forecast_days
    filtered_data = filtered_data[:no_of_values]
    
    if kind == "Temperature":
        filtered_data = [temp["main"]["temp"] for temp in filtered_data]
    if kind == "Sky":
        filtered_data = [sky["weather"][0]["main"] for sky in filtered_data]
    
    return filtered_data

if __name__ == "__main__":
    print(get_data("Tokyo",3,"Sky"))
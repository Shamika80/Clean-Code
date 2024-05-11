import  request

class WeatherDataFetcher:
    def __init__(self, api_key="YOUR_API_KEY_HERE"):  # Add API key
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?" 

    def fetch_weather_data(self, city):
        complete_url = f"{self.base_url}appid={self.api_key}&q={city}"
        response = requests.get(complete_url)
        
        if response.status_code == 200:
            data = response.json()
            return {
                'city': data['name'],
                'temperature': round(data['main']['temp'] - 273.15, 2),  # Convert Kelvin to Celsius
                'condition': data['weather'][0]['description'],
                'humidity': data['main']['humidity']
            }
        else:
            print("Error fetching data. Please check the city name and API key.")
            return {}
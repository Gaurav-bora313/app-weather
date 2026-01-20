import requests
from dotenv import load_dotenv
import os


load_dotenv()

class WeatherData:
    call_count = 0
    def __init__(self, city):
        self.city = city
        self.api = os.getenv("API")
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api}&units=metric"
    
    def getData(self):
        WeatherData.call_count += 1
        print(f"Calls made: {str(WeatherData.call_count)}")
        self.response = requests.get(self.url)
        self.data = self.response.json()
        if self.data['cod'] != 200:
            raise ValueError(f"{self.city} not found")
        else:
            return self.data
        
class Parameters(WeatherData):
    def __init__(self, city):
        super().__init__(city)
        self.data = self.getData()

    def Temp(self):
        main = self.data['main']
        return main['temp']  
    
    def TempFeel(self):
        main = self.data['main']
        return main['feels_like']
    
    def weatherStatus(self):
        main = self.data['weather'][0]
        return main['description'].capitalize()
    
    def minTemp(self):
        main = self.data['main']
        return main['temp_min']
    
    def maxTemp(self):
        main = self.data['main']
        return main['temp_max']
    
    def humidity(self):
        main = self.data['main']
        return main['humidity']
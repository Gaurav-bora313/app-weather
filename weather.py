import requests
from dotenv import load_dotenv
import os

load_dotenv()

class WeatherData:
    def __init__(self, city):
        self.city = city
        self.api = os.getenv("API")
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api}&units=metric"
    
    def getData(self):
        self.response = requests.get(self.url)
        self.data = self.response.json()
        if self.data['cod'] != 200:
            raise ValueError(f"{self.city} not found")
        else:
            return self.data
        
class Parameters(WeatherData):
    def __init__(self, city):
        super().__init__(city)
    
    def Temp(self):
        self.getData()
        main = self.data['main']
        return main['temp']  
    
    def TempFeel(self):
        self.getData()
        main = self.data['main']
        return main['feels_like']
    
    def weatherStatus(self):
        self.getData()
        main = self.data['weather'][0]
        return main['description'].capitalize()
    
    def minTemp(self):
        self.getData()
        main = self.data['main']
        return main['temp_min']
    
    def maxTemp(self):
        self.getData()
        main = self.data['main']
        return main['temp_max']
    
    def humidity(self):
        self.getData()
        main = self.data['main']
        return main['humidity']
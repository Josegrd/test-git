from tkinter import Label
from datetime import datetime
import requests

class WeatherFetcher:
    def __init__(self, city_name, api_key):
        self.city_name = city_name
        self.api_key = api_key
        self.current_temperature = None

    def get_temperature(self):
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': self.city_name,
            'appid': self.api_key,
            'units': 'metric'  # Menggunakan satuan Celsius
        }

        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            temperature = data['main']['temp']
            self.current_temperature = temperature
            return temperature
        except Exception as e:
            print(f"Error: {e}")
            return None

class DateTempManager:
    def __init__(self, master, x_temperature, y_temperature, size_temp, city_name, api_key):
        self.master = master
        self.current_datetime = datetime.now()
        self.weather_fetcher = WeatherFetcher(city_name, api_key)

        # TEMPERATURE
        self.label_temperature = Label(
            self.master,
            text="",
            bg="#ffffff",
            fg="#737373",
            font=("Montserrat", size_temp * -1, "bold")
        )
        self.label_temperature.place(x=x_temperature, y=y_temperature, anchor="nw")

        # Atur agar fungsi update_datetime dipanggil setiap detik (1000 milidetik)
        self.master.after(60000, self.update_datetime)

    def update_datetime(self):
        # Update suhu
        temperature = self.weather_fetcher.get_temperature()
        if temperature is not None:
            formatted_temperature = f"{temperature:.2f}°C"
            self.label_temperature.config(text=formatted_temperature)

        # Atur agar fungsi ini dipanggil setiap detik (1000 milidetik)
        self.master.after(1500, self.update_datetime)

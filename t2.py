class WeatherModel:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_precipitation(self, temperature, humidity):
        return self.a * temperature**2 + self.b * humidity + self.c


def main():
    # Quadratic model coefficients
    a_coefficient = 0.01
    b_coefficient = -0.5
    c_coefficient = 25

    # Instantiate WeatherModel
    weather_model = WeatherModel(a_coefficient, b_coefficient, c_coefficient)

    # Example data
    temperature_data = 28.0
    humidity_data = 0.8

    # Calculate precipitation using the quadratic model
    precipitation_result = weather_model.calculate_precipitation(temperature_data, humidity_data)

    # Print result
    print(f"Temperature: {temperature_data} °C")
    print(f"Humidity: {humidity_data}")
    print(f"Precipitation: {precipitation_result}")


if __name__ == "__main__":
    main()

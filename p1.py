# Stage 1: Hard-coding Variables

def quadratic_solution(a, b, c):
    # Quadratic formula: x = (-b ± sqrt(b^2 - 4ac)) / (2a)
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return None  # No real roots
    else:
        root1 = (-b + (discriminant)**0.5) / (2*a)
        root2 = (-b - (discriminant)**0.5) / (2*a)
        return root1, root2


# Example with hard-coded values
temperature= 1
pressure= -3
humidity= 2

roots = quadratic_solution(temperature, pressure,humidity)
print("Roots:", roots)

# Stage 2: Keyboard Input

def get_coefficients_from_user():
    a = float(input("Enter the temperature: "))
    b = float(input("Enter the pressure: "))
    c = float(input("Enter the humidity: "))
    return a, b, c


# Example with keyboard input
coefficients = get_coefficients_from_user()
roots = quadratic_solution(*coefficients)
print("Roots:", roots)

# Stage 3: Read from a File

import csv

def get_coefficients_from_file(file_path):
  try:
      with open(file_path, 'r') as file:
          reader = csv.DictReader(file)

          # Assume column headings are 'a', 'b', 'c'
          coefficients_list = []
          for row in reader:
              a = float(row['temperature'])
              b = float(row['pressure'])
              c = float(row['humidity'])
              coefficients_list.append((a, b, c))

          return coefficients_list
  except FileNotFoundError:
      print("File not found.")
      return None

# Example with reading from a CSV file
file_path = "sample.csv"
coefficients_list = get_coefficients_from_file(file_path)

if coefficients_list:
    i = 1
    for coefficients in coefficients_list:
        roots = quadratic_solution(coefficients[0], coefficients[1], coefficients[2])
        print(f"Roots for Set {i}: {roots}")
        i += 1
def weather_model(a, b, c):
    """
    This function represents a simplified weather model using a quadratic equation.
    The coefficients a, b, and c correspond to temperature, pressure, and humidity.
    """
    roots = quadratic_solution(a, b, c)

    if roots is None:
        print("No real roots. Unable to predict weather.")
    else:
        # Use the roots to make weather predictions
        root1, root2 = roots
        average_root = (root1 + root2) / 2

        if average_root < 0:
            print("Expect cold weather.")
        elif 0 <= average_root <= 25:
            print("Expect moderate weather.")
        else:
            print("Expect warm weather.")



# Example with reading from a CSV file for weather model
file_path = "sample.csv"
coefficients_list = get_coefficients_from_file(file_path)

if coefficients_list:
    i = 1
    for coefficients in coefficients_list:
        print(f"Weather prediction for Set {i}:")
        weather_model(*coefficients)
        i += 1


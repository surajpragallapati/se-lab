import csv
import matplotlib.pyplot as plt

# Define file path
file_path = "weatherHistory.csv"

# Read data from file
with open(file_path, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

# Extract temperature, humidity, and pressure data
temperatures = [float(row["temperature"]) for row in data]
humidities = [float(row["humidity"]) for row in data]
pressures = [float(row["pressure"]) for row in data]

# Define quadratic equation coefficients
a = 0.01
b = -0.5
c = 25

# Calculate precipitation for each data point
precipitations = [a * temp**2 + b * humidity + c for temp, humidity in zip(temperatures, humidities)]

# Print result for the first data point
print(f"Precipitation: {precipitations[0]}")

# Plotting the graph
plt.figure(figsize=(10, 6))

# Plotting temperature, humidity, pressure, and precipitation
plt.subplot(2, 1, 1)
plt.plot(temperatures, label='Temperature')
plt.plot(humidities, label='Humidity')
plt.plot(pressures, label='Pressure')
plt.title('Weather Parameters over Time')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()

# Plotting precipitation
plt.subplot(2, 1, 2)
plt.plot(precipitations, label='Precipitation', color='red')
plt.title('Precipitation Prediction over Time')
plt.xlabel('Time')
plt.ylabel('Precipitation')
plt.legend()

# Adjust layout for better visualization
plt.tight_layout()

# Show the plot
plt.show()

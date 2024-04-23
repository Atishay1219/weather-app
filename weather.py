import requests

# Replace YOUR_API_KEY with your actual API key
API_KEY = "1affb215ac23292658e57411184b5568"

# Get city name from user input
city = input("Enter city name: ")

# Construct API URL
URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

# Send HTTP request
response = requests.get(URL)


# Check if request was successful
if response.status_code == 200:
    # Parse JSON data
    data = response.json()
    

    # Extract relevant information
    temp = data['main']['temp']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    # Display results
    print(f"Temperature display(in kelvin unit) = {temp}")
    print(f"atmospheric pressure display(in hPa unit) = {pressure/10}")
    print(f"humidity display(in percentage) = {humidity}")
    print(f"description = {description}")
else:
    # If request was not successful, print error message
    print("Error fetching weather data")
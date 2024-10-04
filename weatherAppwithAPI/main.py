# Import necessary libraries
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# Create the main window
root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# Function to get and display weather information
def getWeather():
    try:
        # Get the city name from the input field
        city = textfield.get()

        # Get the location coordinates using Nominatim
        geolocator = Nominatim(user_agent="weatherApp")
        location = geolocator.geocode(city)
        if not location:
            raise ValueError("Location not found")

        # Find the timezone of the location
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    
        # Get the current time in the location's timezone
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="Current Time")

        # Fetch weather data from OpenWeatherMap API
        api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=cea4dbcf43deef00707829c47fc46336"
        response = requests.get(api)
        response.raise_for_status()
        json_data = response.json()

        # Extract weather information from the API response
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = round(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # Update the GUI with weather information
        t.config(text=f"{temp}°")
        c.config(text=f"{condition} | FEELS LIKE {temp}°")
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    # Handle various exceptions
    except requests.RequestException as e:
        messagebox.showerror("Weather App", f"Network error: {e}")
    except (KeyError, IndexError) as e:
        messagebox.showerror("Weather App", f"Error parsing weather data: {e}")
    except ValueError as e:
        messagebox.showerror("Weather App", str(e))
    except Exception as e:
        messagebox.showerror("Weather App", f"An unexpected error occurred: {e}")

# Create and place the search box
Search_image = PhotoImage(file="C:/Users/Ali/Desktop/BEN/YAZILIM/Python/GUIwithPython/weatherAppwithAPI/search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=100, y=40)
textfield.focus()
textfield.bind('<Return>', lambda event: getWeather())

# Create and place the search button
Search_icon = PhotoImage(file="C:/Users/Ali/Desktop/BEN/YAZILIM/Python/GUIwithPython/weatherAppwithAPI/search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# Add the logo
Logo_image = PhotoImage(file="C:/Users/Ali/Desktop/BEN/YAZILIM/Python/GUIwithPython/weatherAppwithAPI/logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# Create the bottom box
Frame_image = PhotoImage(file="C:/Users/Ali/Desktop/BEN/YAZILIM/Python/GUIwithPython/weatherAppwithAPI/box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Create and place the time display
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Create and place labels for weather information
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)
label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)
label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)
label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

# Create labels to display weather data
t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=250, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=430, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=650, y=430)

# Start the main event loop
root.mainloop()

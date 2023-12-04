from lab3.Rectangle import Rectangle 
from lab3.Square import Square
from lab3.Circle import Circle
from lab3.Color import Color
import requests
import json

def get_time():
    response = requests.get("http://worldtimeapi.org/api/timezone/Europe/Moscow")
    return json.loads(response.text)["datetime"]


print("Current time: " + get_time()+"\n")

color = Color(255, 0, 255)
rect = Rectangle(10, 13, color)
print(rect)

square = Square(11, color)
print(square)

circle = Circle(10, color)
print(circle)

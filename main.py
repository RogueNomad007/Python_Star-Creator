
from turtle import *

points = input("number of points?")
length = input("how long?")
points = int(points)
length = int(length)
degrees = 180 / points
degrees = 180 - degrees
i = 0
while i < points:
    forward(length)
    right(degrees)
    degrees = degrees % 360
    i = i + 1

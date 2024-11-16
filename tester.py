import math

def pythagoras(a, b):
  c = math.sqrt(a**2 + b**2)
  print('c = ', c)
  return c

def circle(r):
  area = math.pi * r**2
  print('area = ', area)
  return area

import math

def pythagoras(a, b):

    c = math.sqrt(a**2 + b**2)
    print(f'c = {c}')
    return c

def circle(r):
    
    area = math.pi * r**2
    print(f'area = {area}')
    return area


if __name__ == "__main__":

    pythagoras(3, 4)  

    
    circle(10)  

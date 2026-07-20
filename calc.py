def add(x,y):
    return x+y

def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y!=0:
        return x/y
    else:
        return "Error: Division by zero"
def mod(x,y):
    if y!=0:
        return x%y
    else:
        return "Error: Division by zero"
def floor_div(x,y):
    if y!=0:
        return x//y
    else:
        return "Error: Division by zero"
def pow(x,y):
    return x**y
def sq(x):
    return x**2
def cube(x):
    return x**3
def sqrt(x):
    if x>=0:
        return x**0.5
    else:
        return "Error: Square root of negative number"
def cbrt(x):
    if x>=0:
        return x**(1/3)
    else:
        return -(-x)**(1/3)


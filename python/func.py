def hello_world():
    return "Hello, world!"
def add(x,y):
    return x + y
def multiply(x,y):
    return x * y
def greeting(name):
    print(f"Good morning, {name}!")
def divide(x,y):
    return x / y

def main():
    x,y = map(int,input("Enter two numbers\n").split())
    print(f"{x} * {y} = {multiply(x,y)}")
    greeting("John")
    try:
        print(f"{x} / {y} = {divide(x,y)}")
    except ZeroDivisionError:
        print("Division by zero!")
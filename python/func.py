def hello_world():
    return "Hello, world!"


def multiply(x: float, y: float):
    return x * y


def greeting(name: str):
    print(f"Good morning, {name}!")


def divide(x: float, y: float):
    return x / y


def main():
    x, y = map(int, input("Enter two numbers\n").split())
    print(f"{x} * {y} = {multiply(x, y)}")
    greeting("John")
    try:
        print(f"{x} / {y} = {divide(x, y)}")
    except ZeroDivisionError:
        print("Division by zero!")

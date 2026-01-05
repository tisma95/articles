
def hello():
    print("hello()::called")
    return "Hello"


def hello(name):
    print(f"hello()::called with parameter name='{name}'")
    return f"Hello {name}"


def hello(name):
    print(f"hello()::called with parameter name='{name}'")
    response = f"Hello {name}"
    print(f"hello()::executed with result:'{response}'")
    return response

def getName():
    print("getName():called")
    name = input("Enter your name:")
    print(f"getName()::executed with result name='{name}'")
    return name


def main():
    print("main():called")
    name = getName()
    print(f"main()::executed getName() with result name='{name}'")
    hello(name)

main()
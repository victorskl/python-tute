subscribers = []


def hello_world():
    print("Hello, world.")
    for subscriber in subscribers:
        subscriber()

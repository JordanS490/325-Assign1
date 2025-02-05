def decore(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decore
def say_hello():
    print("Hello!")

say_hello()
def my_deca(func):
    def inner():
        print("Decorator work")
        func()
        print("Decorator stopped")

    return inner


def my_func(): print("Salom Dunyo")


a = my_deca(my_func)
a()

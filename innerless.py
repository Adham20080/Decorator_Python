def my_deca(func):
    def inner():
        print("Decorator work")
        func()
        print("Decorator stopped")

    return inner


# def my_func(): print("Salom Dunyo")


# a = my_deca(my_func)
# a()

@my_deca
def my_func2():
    a = []
    for i in range(5000000 + 1):
        a.append(i)


my_func2()

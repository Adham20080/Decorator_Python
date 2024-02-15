def my_deca(func):
    def inner(a):
        print("Decorator work")
        func(a)
        print("Decorator stopped")

    return inner


# def my_func(): print("Salom Dunyo")


# a = my_deca(my_func)
# a()

# @my_deca
# def my_func2():
#     a = []
#     for i in range(5000000 + 1):
#         a.append(i)
#
#
# my_func2()


@my_deca
def my_func3(a: int):
    if a % 2:
        print(f"Bu Toq son: {a}")
    else:
        print(f"Bu Juft son: {a}")


my_func3(5)

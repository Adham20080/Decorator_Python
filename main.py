def hello(name):
    def ret_name():
        return "Salom " + name + " 😎"

    return ret_name()


print(hello("Ahmadjon"))


# def mull(n: int) -> int:
#     def mul(x: int) -> int:
#         return x * n
#
#     return mul  # noqa
#
#
# mul_th = mull(3)
# mul_ff = mull(5)
# print(mul_th(9))  # 27 # noqa
# print(mul_ff(3))  # 15 # noqa
# print(mul_ff(mul_th(2)))  # 30 # noqa

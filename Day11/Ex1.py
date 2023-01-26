# Định nghĩa 4 hàm sum, subtract, divide, multiply với 2 đôi số truyền vào hàm
def sum(x, y):
    return x+y


print(sum(3, 2))


def subtract(x, y):
    return x-y


print(subtract(5, 1))


def divide(x, y):
    if y == 0:
        return("Không thể chia cho 0")
    return x/y


print(divide(5, 0))


def multiply(x, y):
    return x*y


print(multiply(2, 4))

"""Operators."""


def add(x, y):
    """Add x to y."""
    total = x + y
    return total


def sub(x, y):
    """Subtract y from x."""
    subtract = x - y
    return subtract


def multiply(x, y):
    """Multiply x by y."""
    product = x * y
    return product


def div(x, y):
    """Divide x by y."""
    division = x / y
    return division


def modulus(x, y):
    """Divide x by y and return remainder. Use an arithmetic operator."""
    remnant = x % y
    return remnant


def floor_div(x, y):
    """Divide x by y and floor the value. Use an arithmetic operator."""
    floored_value = x // y
    return floored_value


def exponent(x, y):
    """Calculate x where y is an exponent."""
    exp = x ** y
    return exp


def first_greater_or_equal(x, y):
    """If x is greater or equal than y then return True. If not then return False."""
    if x >= y:
        return True
    else:
        return False


def second_less_or_equal(x, y):
    """If y is less or equal than x then return True. If not then return False."""
    if y <= x:
        return True
    else:
        return False


def x_is_y(x, y):
    """If x same as y then return True. If not then return False."""
    if x == y:
        return True
    else:
        return False


def x_is_not_y(x, y):
    """If x is not same as y then return True. If not then return False."""
    if x != y:
        return True
    else:
        return False


def if_else(a, b, c, d):
    """
    Create a program that has 4 numeric parameters. Multiply parameters 1-2 (multiply a by b) by each other and divide
    parameters 3-4 (divide c by d) by each other. Next check and return the greater value. If both values are the same
    then return 0 (number zero).
    """
    total = a * b
    division = c / d
    if total > division:
        return total
    elif total == division:
        return 0
    else:
        return division


def surface(a, b):
    """Add the missing parameters to calculate the surface. Calculate and return the value of surface."""
    area = a * b
    return area


def volume(a, b, c):
    """Add the missing parameters to calculate the volume. Calculate and return the value of volume."""
    vol = a * b * c
    return vol

# if __name__ == '__main__':
#     print(add(1, -2))  # -1
#     print(sub(5, 5))  # 0
#     print(multiply(5, 5))  # 25
#     print(div(15, 5))  # 3
#     print(modulus(9, 3))  # 0
#     print(floor_div(3, 2))  # 1
#     print(exponent(5, 5))  # 3125
#     print(first_greater_or_equal(1, 2))  # False
#     print(second_less_or_equal(5, 5))  # True
#     print(x_is_y(1, 2))  # False
#     print(x_is_not_y(1, 2))  # True
#     print(if_else(1, 3, 5, 99))  # 3
#     print(if_else(2, 1, 10, 5))  # 0
# print(surface(1, 2)) # 2
# print(volume(5, 5, 5)) # 125

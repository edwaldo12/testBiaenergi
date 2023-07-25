def multiply(x, y):
    if x == 0 or y == 0:
        return 0

    if x < 0:
        return -multiply(-x, y)

    if not isinstance(x, int):
        raise ValueError("The 'x' value must be an integer.")

    if not isinstance(y, int):
        raise ValueError("The 'y' value must be an integer.")

    total = 0
    while x > 0:
        total += y
        x -= 1
    return total


print(multiply(5, 2))

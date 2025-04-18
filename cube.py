def cube(n):
    return n * n * n


def byThree(n):
    if n % 3 == 0:
        return cube(n)
    else:
        return "invalid"


print(byThree(63.0))

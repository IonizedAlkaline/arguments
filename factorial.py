def fact(n):
    """this is recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))
print(fact.__doc__)

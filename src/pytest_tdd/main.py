def return_same(param):
    return param


def append_to_list(param, items=[]):
    return items.append(param)


def is_palindrome(phrase):
    pass


def complex_(a, b, c):
    if a > b:
        if b < c:
            return a * c, b
        elif a + b == c:
            return a
    elif c + a == 1:
        return a ^ 2

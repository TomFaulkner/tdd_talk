def return_same(param):
    return param


def append_to_list(param, items=None):
    if not items:
        items = []
    items.append(param)
    return items


def is_palindrome(phrase):
    return (
        phrase.lower().replace('?', '').replace(' ', '')
        == ''.join(reversed(phrase.lower().replace('?', '').replace(' ', '')))
    )


def complex_(a, b, c):
    if a > b:
        if b < c:
            return a * c, b
        elif a + b == c:
            return a
    elif c + a == 1:
        return a ^ 2

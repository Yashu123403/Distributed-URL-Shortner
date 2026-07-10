import string

characters = string.digits + string.ascii_letters


def encode(num):
    """
    Convert integer ID to Base62 string
    """

    if num == 0:
        return characters[0]

    result = ""

    while num:
        num, remainder = divmod(num, 62)
        result = characters[remainder] + result

    return result


def decode(code):
    """
    Convert Base62 string back to integer ID
    """

    num = 0

    for char in code:
        num = num * 62 + characters.index(char)

    return num
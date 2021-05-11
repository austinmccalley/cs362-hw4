def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def volume(side1, side2, side3):
    """ Check each side to see if its a valid int or float """
    side1S = str(side1)
    side2S = str(side2)
    side3S = str(side3)

    assert is_number(side1S)
    assert is_number(side2S)
    assert is_number(side3S)

    return side1 * side2 * side3

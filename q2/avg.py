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

def avg(list):
    length = len(list)
    if length == 0:
        return 0
    for e in list:
        assert is_number(str(e))
    tSum = sum(list)

    return tSum/length

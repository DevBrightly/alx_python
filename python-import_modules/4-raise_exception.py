def raise_exception():
    try:
        x = "string"
        y = 5

        result = x + y
    except TypeError:
        raise

for number in range(10):
    for number2 in range(number + 1, 10):
        print("{:02}".format(number * 10 + number2), end=", " if number != 8 else " ")
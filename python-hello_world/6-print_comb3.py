for tens_digit in range(10):
    for unit_digit in range(tens_digit, 10):
        if tens_digit != unit_digit:
            if tens_digit < 8:
                print("{}{}".format(tens_digit, unit_digit), end=', ')
            else:
                print("{}{}".format(tens_digit, unit_digit), end='\n')
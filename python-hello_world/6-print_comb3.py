print(", ".join("{:02}".format(number * 10 + number2) for number in range(10) for number2 in range(number + 1, 10)))
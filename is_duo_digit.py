def is_duo_digit(number):
    res =set()
    for digit in str(number):
        res.add(digit)

    if len(res) > 2 :
        return 0

    return 1



# print(is_duo_digit(102))
print(is_duo_digit(12))
def even_numbers(beginning: int, maximum: int):
    if beginning % 2 != 0:
        beginning += 1
    while beginning <= maximum:
        yield beginning
        beginning += 2


if __name__ == "__main__":
    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)

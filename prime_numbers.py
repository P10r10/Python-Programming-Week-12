def is_prime(n: int) -> bool:
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_numbers():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1


if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))

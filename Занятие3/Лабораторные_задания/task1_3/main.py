def func_(a: int) -> list:
    list_simple_numbers = []
    for current_number in range(a + 1):
        m = 0  # количество множителей числа i
        for n in range(1, current_number + 1):
            if current_number % n == 0:
                m = m + 1
        if m == 2:
            list_simple_numbers.append(current_number)

    return list_simple_numbers


def func_1(number, list_prime_numbers):
    prime_factors = []
    while number != 1:
        for prime_number in list_prime_numbers:
            while number % prime_number == 0:
                prime_factors.append(prime_number)
                number = number // prime_number

    return prime_factors


if __name__ == "__main__":
    s = 63
    list_ = func_(s)
    print(list_)
    list_1 = func_1(s, list_)
    print(list_1)



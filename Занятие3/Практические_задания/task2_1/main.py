def pow_func(base, pow_=2):
    # base ** pow_ -> реализовать через цикл while
    res = 1
    n = 0
    while n < pow_:
        res = res * base  # res *= base
        n = n + 1  # pow_ -= 1

    return res


if __name__ == "__main__":
    a = 5
    n = 3

    print(pow_func(a, n))

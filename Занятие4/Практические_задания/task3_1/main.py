if __name__ == "__main__":
    cart = {
        "apple": 80,
        "orange": 65,
        "banana": 40
    }
    print(cart.keys())

    sum_ = 0
    for fruit in cart:
        sum_ += cart[fruit]
        print(fruit, cart[fruit])  # получаем значение по ключу

    print(sum_)
    print(sum(cart.values()))

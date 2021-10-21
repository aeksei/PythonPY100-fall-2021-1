def remove_whitespace(str_):
    list_words = str_.split()
    print(list_words)

    return " ".join(list_words)


if __name__ == "__main__":
    str_with_space = "    123.    test   print test11    "  # исходная строка
    print(str_with_space)
    print(remove_whitespace(str_with_space))

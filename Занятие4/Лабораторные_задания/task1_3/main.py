def function(list_):
    return len([i for i in list_ if i % 2 ==0])


if __name__ == "__main__":
    list_ = [1,2,3,4,5,6,7,8,9]
    print(function(list_))
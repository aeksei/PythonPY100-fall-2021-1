if __name__ == "__main__":
    # matrix = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]

    count_row = 10
    count_col = 10
    matrix = [
        [i * j for j in range(1, count_col)]
        for i in range(1, count_row)
    ]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(f"{matrix[row][col]:2}", end=" ")
        print()




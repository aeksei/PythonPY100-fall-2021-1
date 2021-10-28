from logic import (
    init_field, is_win,
    player_step, enemy_step, is_avalible_ceil
)


def main():
    field = init_field()
    print_field(field)

    first_player, second_player = "X", "O"

    while True:
        x, y = get_step(first_player)
        player_step(x, y, first_player, field)
        print_field(field)

        if is_win(field, first_player):
            print(f"Победил игрок {first_player}")
            break

        if not is_avalible_ceil(field):
            print("Ничья")
            break

        x, y = get_step(second_player)
        enemy_step(x, y, second_player, field)
        print_field(field)

        if is_win(field, second_player):
            print(f"Победил игрок {second_player}")
            break

        if not is_avalible_ceil(field):
            print("Ничья")
            break



    print("Игра закончена")


def print_field(field) -> None:
    """

    :param field:
    :return:
    """
    for row in field:
        for ceil in row:
            print(ceil, end="")
        print()


def get_step(player_symbol: str) -> tuple[int, int]:
    while True:
        step = input(f"Игрок {player_symbol} "
                     f"введите две координаты через пробел: ")
        coords = step.split()
        if len(coords) < 2:
            print("Введено слишком мало координат")
            continue
        elif len(coords) > 2:
            print("Введено слишком много координат")
            continue

        x_str: str
        y_str: str
        x_str, y_str = coords

        if not x_str.isdigit():
            print("Координата x не число")
            continue

        if not y_str.isdigit():
            print("Координата y не число")
            continue

        x, y = int(x_str), int(y_str)

        if not 1 <= x <= 3:
            print("Неверная координата x")
            continue

        if not 1 <= y <= 3:
            print("Неверная координата y")
            continue

        # todo проверка перезаписи хода

        return x-1, y-1







if __name__ == '__main__':
    main()

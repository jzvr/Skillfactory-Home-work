import numpy as np


def game_core_v2(number):
    count = 1
    a_start = 0
    b_end = 101
    b1_middle = 50
    while number != b1_middle:  # Рассчет идет по делению отрезков на 2
        count += 1
        if number < b1_middle:
            b_end = b1_middle
            b1_middle = ((b_end - a_start)//2)+a_start
        elif number > b1_middle:
            a_start = b1_middle
            b1_middle = ((b_end - a_start)//2) + a_start
    return(count)   # выход из цикла, если угадали


def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v2)
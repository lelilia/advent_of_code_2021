""" Advent of Code 2021 day 21 """


def play1(p1, p2):
    dice = 1
    p1_score = p2_score = 0
    turn = 0
    while p1_score < 1000 and p2_score < 1000:
        if turn % 2 == 0:
            p1 = (p1 + dice + dice + 1 + dice + 2) % 10
            p1_score += p1 + 1
        else:
            p2 = (p2 + 3 * dice + 3) % 10
            p2_score += p2 + 1
        turn += 1
        dice = (dice + 3) % 10
        dice = 100 if dice == 0 else dice
    return min(p1_score, p2_score) * turn * 3


def get_multitude(i):
    if i == 3 or i == 9:
        return 1
    elif i == 4 or i == 8:
        return 3
    elif i == 5 or i == 7:
        return 6
    return 7


def play(p1s, p2s, p1, p2, turn, multitude):
    global p1_win, p2_win
    if p1s >= 21:
        p1_win += multitude
        return
    elif p2s >= 21:
        p2_win += multitude
        return

    for i in range(3, 10):
        mi = multitude * get_multitude(i)

        if turn % 2 == 0:
            p1_i = (p1 + i) % 10
            play(p1s + p1_i + 1, p2s, p1_i, p2, turn + 1, mi)
        else:
            p2_i = (p2 + i) % 10
            play(p1s, p2s + p2_i + 1, p1, p2_i, turn + 1, mi)


if __name__ == "__main__":

    p1 = 4 - 1
    p2 = 5 - 1
    p1_win = p2_win = 0

    print("Part 1:\t", play1(p1, p2))

    play(0, 0, p1, p2, 0, 1)
    print("Part 2:\t", max(p1_win, p2_win))

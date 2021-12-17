def hit_target(x, y, target):
    return target[0] <= x <= target[1] and target[2] <= y <= target[3]


def shoot(vx, vy):
    x = y = 0
    i = 0
    max_y = 0
    while True:
        x += vx
        vx = vx - 1 if vx > 0 else 0
        y += vy - i

        max_y = max(y, max_y)
        i += 1
        if hit_target(x, y, target):
            return True, max_y
        if x > max(target[0], target[1]) or y < min(target[2], target[3]):
            return False, 0


def find_minimal_vx(target):
    vx = 0
    while x_endpoint(vx) < target[0]:
        vx += 1
    return vx


def x_endpoint(vx):
    return sum(range(vx + 1))


if __name__ == "__main__":

    target = [143, 177, -106, -71]
    max_height = 0
    hit_count = 0

    vx = find_minimal_vx(target)

    for vx_i in range(vx, target[1] + 1):
        for vy_i in range(target[2], -target[2] + 1):
            r, max_y = shoot(vx_i, vy_i)
            if r:
                max_height = max(max_height, max_y)
                hit_count += 1

    print("Part 1:\t", max_height)
    print("Part 2:\t", hit_count)

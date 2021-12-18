class Tree:
    def __init__(self, val=None, parent=None, left=None, right=None):
        self.parent = parent

        if type(val) == list:
            self.value = None
            self.left = Tree(val[0], self)
            self.right = Tree(val[1], self)
        else:
            self.value = val
            self.left = None
            self.right = None

    def __repr__(self):
        return str(self.tree_list())

    def __add__(self, other):
        new_root = Tree()
        right = Tree(other, new_root)
        left = self
        left.parent = new_root
        new_root.left = left
        new_root.right = right
        new_root.reduce()
        return new_root

    def tree_list(self):
        if self.value != None:
            return self.value
        else:
            left = self.left.tree_list()
            right = self.right.tree_list()
            return [left, right]

    def explode(self, depth):
        if self.left:
            if depth == 4 and not self.left.left and not self.right.left:
                left_neighbour = self.parent
                old_value = self
                while (left_neighbour and left_neighbour.left == old_value):
                    old_value = left_neighbour
                    left_neighbour = left_neighbour.parent
                if left_neighbour:
                    left_neighbour = left_neighbour.left
                while left_neighbour and left_neighbour.right:
                    left_neighbour = left_neighbour.right

                right_neighbour = self.parent
                old_value = self
                while (right_neighbour and right_neighbour.right == old_value):
                    old_value = right_neighbour
                    right_neighbour = right_neighbour.parent
                if right_neighbour:
                    right_neighbour = right_neighbour.right
                while right_neighbour and right_neighbour.left:
                    right_neighbour = right_neighbour.left

                if left_neighbour:
                    left_neighbour.value += self.left.value
                if right_neighbour:
                    right_neighbour.value += self.right.value
                self.left = None
                self.right = None
                self.value = 0

                return True
            return self.left.explode(depth + 1) or self.right.explode(depth+1)
        return False

    def split(self):
        if self.value and self.value > 9:
            self.left = Tree(self.value // 2, self)
            self.right = Tree((self.value + 1) // 2, self)
            self.value = None
            return True
        if self.left:
            return self.left.split() or self.right.split()
        return False

    def reduce(self):
        while self.explode(0):
            continue
        if self.split():
            self.reduce()

    def magnitude(self):
        if self.value != None:
            return self.value
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()


if __name__ == "__main__":

    with open("input18.txt") as f:
        data = f.read().strip().split("\n")

    root = Tree(eval(data[0]))
    for line in data[1:]:
        root = root + eval(line)

    print("Part 1:\t", root.magnitude())

    maximum_magnitude = 0
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            r = Tree(eval(data[i]))
            r += eval(data[j])
            maximum_magnitude = max(maximum_magnitude, r.magnitude())
            r = Tree(eval(data[j]))
            r += eval(data[i])
            maximum_magnitude = max(maximum_magnitude, root.magnitude())
    print(maximum_magnitude)

    # for i in range(len(data) - 1):
    #     for j in range(2):
    #         root = Tree(eval(data[j % 2]))
    #         root = root + eval(data[(j+1) % 2])
    #         maximum_magnitude = max(maximum_magnitude, root.magnitude())
    # print(maximum_magnitude)
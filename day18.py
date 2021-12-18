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
        self.parent = new_root
        new_root.left = self
        other.parent = new_root
        new_root.right = other
        new_root.reduce()
        return new_root

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def tree_list(self):
        if self.value != None:
            return self.value
        else:
            left = self.left.tree_list()
            right = self.right.tree_list()
            return [left, right]

    def get_next_left_neighbour(self):
        next_left = self.parent
        old_value = self
        while next_left and next_left.left == old_value:
            old_value = next_left
            next_left = next_left.parent
        if next_left:
            next_left = next_left.left
        while next_left and next_left.right:
            next_left = next_left.right
        return next_left

    def get_next_right_neighbour(self):
        next_right = self.parent
        old_value = self
        while next_right and next_right.right == old_value:
            old_value = next_right
            next_right = next_right.parent
        if next_right:
            next_right = next_right.right
        while next_right and next_right.left:
            next_right = next_right.left
        return next_right

    def explode(self, depth):
        if self.left:
            if depth == 4 and not self.left.left and not self.right.left:
                next_left = self.get_next_left_neighbour()
                next_right = self.get_next_right_neighbour()
                if next_left:
                    next_left.value += self.left.value
                if next_right:
                    next_right.value += self.right.value
                self.left = None
                self.right = None
                self.value = 0

                return True
            return self.left.explode(depth + 1) or self.right.explode(depth + 1)
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

    trees = [Tree(eval(d)) for d in data]

    print("Part 1:\t", sum(trees).magnitude())

    maximum_magnitude = 0

    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue
            t1 = Tree(eval(data[i]))
            t2 = Tree(eval(data[j]))

            maximum_magnitude = max(maximum_magnitude, (t1 + t2).magnitude())

    print("Part 2:\t", maximum_magnitude)

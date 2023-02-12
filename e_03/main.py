class Node:
    def __init__(self) -> None:
        self.parent = []
        self.child = []
        self.temp = []

    def __str__(self) -> str:
        return str(f'Root: {self.parent} Child: {self.child}')

    def add(self, data):
        if(len(self.parent) > 1):
            self.parent.sort()
        if(len(self.parent) >= 3):
            left = self.parent[0]
            middle = self.parent[1]
            right = self.parent[2]
            self.split(left, middle, right)
            return self.temp

        self.parent.append(data)
        self.temp.append(data)

    def split(self, left, middle, right):
        self.temp[0] = middle
        self.temp[1] = left
        self.temp[2] = right


class Trees:
    def __init__(self) -> None:
        self.root = None
        self.result = []

    def insert(self, data):
        if (len(self.result) <= 3):
            node = Node()
            temp = node.add(data)
            #self.result = temp
            print(temp)


class Main:
    def __init__(self) -> None:
        self.test = [13, 7, 24, 15, 4, 29, 20, 16, 19, 1, 5, 22, 17]
        self.two_three_tree()

    def two_three_tree(self):
        tree = Trees()
        for val in self.test:
            tree.insert(val)


if __name__ == "__main__":
    main = Main()

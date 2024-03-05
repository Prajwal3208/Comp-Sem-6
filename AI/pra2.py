import heapq

class Node:
    def __init__(self, data, level, direction=""):
        self.data = data
        self.level = level
        self.direction = direction
        self.fval = 0  

    def generate_child(self):
        x, y = self.find(self.data, '_')
        val_list = [[x, y - 1, "left"], [x, y + 1, "right"], [x - 1, y, "up"], [x + 1, y, "down"]]
        children = []

        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, i[2])
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):
        if 0 <= x2 < len(self.data) and 0 <= y2 < len(self.data):
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, puz, x):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if puz[i][j] == x:
                    return i, j

class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []

    def accept(self):
        puz = []
        print("Enter the puzzle matrix (use '_' for the blank space):")
        for _ in range(self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self, start, goal):
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        temp = 0
        for i in range(self.n):
            for j in range(self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def process(self):
        print("Enter the start state:")
        start = self.accept()
        print("Enter the goal state:")
        goal = self.accept()

        start_node = Node(start, 0)
        start_node.fval = self.f(start_node, goal)
        self.open.append(start_node)
        print("\n\n")
        while True:
            cur_node = self.open[0]
            for i in cur_node.data:
                for j in i:
                    print(j, end=" ")
                print("")
            print(f"Move: {cur_node.direction}")
            print(f"Heuristic Value: {self.h(cur_node.data, goal)}")

            if self.h(cur_node.data, goal) == 0:
                print("Goal State Reached!")
                break

            for child_node in cur_node.generate_child():
                child_node.fval = self.f(child_node, goal)

                similar_state = next((node for node in self.open if node.data == child_node.data and node.fval < child_node.fval), None)
                if similar_state:
                    continue

                self.open.append(child_node)

            del self.open[0]
            self.open.sort(key=lambda x: x.fval, reverse=False)

puz = Puzzle(3)
puz.process()


class NQueensBacktracking:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        
        for i in range(row):
            if self.board[i][col]:
                return False

      
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j]:
                return False

        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.board[i][j]:
                return False

        return True

    def solve_backtracking(self, row):
        if row == self.n:
            self.solutions.append([row[:] for row in self.board])
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.solve_backtracking(row + 1)
                self.board[row][col] = 0

    def print_solutions(self):
        for solution in self.solutions:
            for row in solution:
                print(row)
            print()


n = 8
solver = NQueensBacktracking(n)
solver.solve_backtracking(0)
solver.print_solutions()


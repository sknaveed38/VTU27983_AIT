def solve_n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def backtrack(row):
        if row == n:
            solutions.append(["".join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

    backtrack(0)

    # Print number of solutions
    print(len(solutions))
    # Print each solution
    for sol in solutions:
        for line in sol:
            print(line)
        print()  # blank line between solutions


if __name__ == "__main__":
    n = int(input().strip())
    solve_n_queens(n)

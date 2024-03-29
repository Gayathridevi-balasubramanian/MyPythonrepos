from itertools import product

def solve_sudoku(puzzle):
    for(row,col) in product(range(0,9),repeat=2):
        if puzzle[row][col] ==0:
            for num in range(1,10):
                allowed = True
                for i in range(0,9):
                    if num in (puzzle[i][col],puzzle[row][i]):
                        allowed = False
                        break
                for(i,j) in product(range(0,3),repeat= 2):
                    if puzzle[row - row % 3 + i ][col - col %3 +j]==num:
                        allowed = False
                        break
                if allowed:
                    puzzle[row][col] = num
                    if trial := solve_sudoku(puzzle):
                        return trial
                    puzzle[row][col] = 0
            return False
    return puzzle

def print_sudoku(puzzle):
    # replace zeroes with dashes
    puzzle = [['*' if num == 0 else num for num in row] for row in puzzle]
    print()
    for row in range(0,9):
        if((row % 3 == 0) and (row !=0 )):
            print('-'* 33)
        for col in range(0,9):
            if((col % 3 == 0) and (col != 0)):
                print('|', end='')
            print(f'{puzzle[row][col]}',end ='')
        print()
    print()
test_puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1, 9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9]]


# commands used in solution video for reference
if __name__ == '__main__':
    print_sudoku(test_puzzle)
    solution = solve_sudoku(test_puzzle)
    print_sudoku(solution)

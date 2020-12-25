def main():
    def get_puzzle(txt):
        puzzle = []
        f = open(txt, 'r')
        for x in f:
            puzzle.append(list(map(int, x.split())))
            print(list(map(int, x.split())))
        return puzzle

    def empty_slots(puzzle):
        #checks to see if there is a spot on the puzzle needed to be changed
        for x in range(len(puzzle)):
            for j in range(len(puzzle)):
                if puzzle[x][j] == 0:
                    return x, j #--> row, col
                    # returns to row/col to check for validity in being unique.
        return None, None
        # None, None --> there are no longer any empty slots

    def is_valid(puzzle, row, col, num):
        if check_col(puzzle, col, num) and check_rows(puzzle, row, num) and check_squares_3by3(puzzle, row, col, num):
            return True
        return False


    def check_rows(puzzle, row, num):
        #checks if the num is already in the row.
        for x in puzzle[row]:
            if num == x:
                return False
        return True

    def check_col(puzzle, cols, num):
        col = []
        for x in range(len(puzzle)):
            col.append(puzzle[x][cols])
        #creetes a list of the nums in the given column.

        #checks if the num is in the col.
        if num in col:
            return False
        return True

    def check_squares_3by3(puzzle, row, col, num):
        col = (col//3) * 3
        row = (row//3) * 3
        #i started the range with col b/c of the logic. See puzzle_logic.txt
        for x in range(col, col + 3):
            for y in range(row, row + 3):
                #it goes y and x first because you want to read it by row-col
                if num == puzzle[y][x]:
                    return False
        return True

    def solver(puzzle):
        row, col = empty_slots(puzzle)

        #base conditon
        if row == None:
            return True

        for num in range(1,10):
            if is_valid(puzzle, row, col, num):
                puzzle[row][col] = num
                if solver(puzzle):
                    return True

            puzzle[row][col] = 0


        return False

    def create_ans_file(puzzle):
        f = open('puzzle_solution.txt', 'w+')
        for x in puzzle:
            for num in x:
                f.write(str(num) + " ")
            f.write("\n")

    file_name = 'puzzle.txt'
    print("-------------------------------------")
    puzzle = get_puzzle(file_name)
    print("-------------------------------------")
    solver(puzzle)
    create_ans_file(puzzle)



if __name__ == '__main__':
    main()


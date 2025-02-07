def load_input(file_path):
    puzzle_grid = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.rstrip("\n")
            puzzle_grid.append(line)
    return puzzle_grid

def search(puzzle_grid, loc_x, loc_y):
    directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
    xmas_count = 0
    xmin = 0
    xmax = len(puzzle_grid[0])
    ymin = 0
    ymax = len(puzzle_grid)

    for dx, dy in directions:
        slice = None
        if loc_x + 3 * dx >= 0 and loc_x + 3 * dx < xmax and loc_y - 3 * dy >= 0 and loc_y - 3 * dy < ymax:
            slice = [puzzle_grid[loc_y - dy * k][loc_x + dx * k] for k in range(4)]
            slice = ''.join(slice)


        if slice == 'XMAS':
            xmas_count += 1

    return xmas_count

def x_search(puzzle_grid, loc_x, loc_y):
    if puzzle_grid[loc_y][loc_x] != 'A':
        return 0

    xmin = 0
    xmax = len(puzzle_grid[0])
    ymin = 0
    ymax = len(puzzle_grid)

    if loc_x == 0 or loc_x == xmax-1 or loc_y == 0 or loc_y == ymax - 1:
        return 0

    diag = [puzzle_grid[loc_y - 1][loc_x-1], puzzle_grid[loc_y][loc_x], puzzle_grid[loc_y+1][loc_x+1]]
    anti_diag = [puzzle_grid[loc_y+1][loc_x-1], puzzle_grid[loc_y][loc_x], puzzle_grid[loc_y-1][loc_x+1]]

    diag.sort()
    anti_diag.sort()

    diag = ''.join(diag)
    anti_diag = ''.join(anti_diag)

    if diag == "AMS" and anti_diag == "AMS":
        return 1

    return 0
    
    

def partA(file_path):
    puzzle_grid = load_input(file_path)
    xmax = len(puzzle_grid[0])
    ymax = len(puzzle_grid)

    matches = 0
    
    for x in range(xmax):
        for y in range(ymax):
            matches += search(puzzle_grid, x, y)

    return matches
            

def partB(file_path):
    puzzle_grid = load_input(file_path)
    xmax = len(puzzle_grid[0])
    ymax = len(puzzle_grid)

    matches = 0

    for x in range(xmax):
        for y in range(ymax):
            matches += x_search(puzzle_grid, x, y)

    return matches


if __name__ == "__main__":
    print(f"Part A test: {partA('test_input.txt')}")
    print(f"Part A: {partA('input.txt')}")

    print(f"Part B test: {partB('test_input.txt')}")
    print(f"Part B: {partB('input.txt')}")


    puzzle_grid = load_input('test_input.txt')

    search(puzzle_grid, 1,9)



    

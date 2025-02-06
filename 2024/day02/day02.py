def load_data(file_path):
    reports = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.rstrip("\n")
            levels = [int(x) for x in line.split(" ")]

            reports.append(levels)

    return reports


def is_safe(levels, min_diff = 1, max_diff = 3):
    n = len(levels)
    is_increasing = all([levels[i] - levels[i+1] > 0 for i in range(n-1)])
    is_decreasing = all([levels[i] - levels[i+1] < 0 for i in range(n-1)])

    diffs = [abs(levels[i] - levels[i+1]) for i in range(n-1)]

    if not is_increasing and  not is_decreasing:
        return False

    min_diff_ok = all([diff >= min_diff for diff in diffs])
    max_diff_ok = all([diff <= max_diff for diff in diffs])

    return min_diff_ok and max_diff_ok

def is_safe_v2(levels, min_diff = 1, max_diff = 3):
    if is_safe(levels):
        return True

    n = len(levels)
    for ii in range(n):
        L = [levels [jj] for jj in range(n) if ii != jj]
        if is_safe(L):
            return True

    return False

def partA(file_path):
    levels = load_data(file_path)

    safe_count = 0
    for level in levels:
        safe_count += int(is_safe(level))

    return safe_count

def partB(file_path):
    levels = load_data(file_path)

    safe_count = 0
    for level in levels:
        safe_count += int(is_safe_v2(level))

    return safe_count

if __name__ == "__main__":
    print(f"Part A test: {partA('test_input.txt')}")
    print(f"Part A: {partA('input.txt')}")

    print(f"Part B test: {partB('test_input.txt')}")
    print(f"Part B: {partB('input.txt')}")
    

import re

def load_data(file_path):
    lines = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.rstrip("\n")
            lines.append(line)
            
    return lines

def val_mult_command(mult_str):
    # mult_str has form mult(x,y)

    vals = mult_str.rstrip(")")
    vals = vals.lstrip("mul(")
    x, y = vals.split(",")
    return int(x) * int(y)

def partA(file_path):
    match_str = "mul\(\d{1,3}\,\d{1,3}\)"
    lines = load_data(file_path)

    total = 0

    for line in lines:
        matches = re.findall(match_str, line)
        for command in matches:
            total += val_mult_command(command)

    return total

def partB(file_path):
     match_str = "mul\(\d{1,3}\,\d{1,3}\)"
     new_match_str = f"{match_str}|do\(\)|don\'t\(\)"
     lines = load_data(file_path)

     mult_enabled = True
     total = 0

     for line in lines:
         matches = re.findall(new_match_str, line)
         for command in matches:
             if command == "do()":
                 mult_enabled = True
             elif command == "don't()":
                 mult_enabled = False
             else:
                 if mult_enabled:
                     total += val_mult_command(command)
     return total

if __name__ == "__main__":
    print(f"Part A test: {partA('test_input.txt')}")
    print(f"Part A: {partA('input.txt')}")

    print(f"Part B test: {partB('test_input_b.txt')}")
    print(f"Part B: {partB('input.txt')}")

def load_data(file_path):
    col1 = []
    col2 = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.rstrip("\n")
            L = line.split(" ")
            a = L[0]
            b = L[-1]
            col1.append(int(a))
            col2.append(int(b))

    col1.sort()
    col2.sort()

    return col1, col2



def partA(file_path):
    col1, col2 = load_data(file_path)

    val = 0
    for ii in range(len(col1)):
        val += abs(col1[ii] - col2[ii])

    return val

def count_dict(my_list):
    d = {}

    for x in my_list:
        try:
            d[x] += 1
        except:
            d[x] = 1

    return d

def partB(file_path):
    col1, col2 = load_data(file_path)

    count_1_dict = count_dict(col1)
    count_2_dict = count_dict(col2)

    val = 0

    for key, count in count_1_dict.items():
        val += key * count * count_2_dict.get(key, 0)

    return val
        

    


if __name__ == "__main__":
#    print(f"Test value part A: {partA('test_input.txt')}")
#    print(f"Answer part A: {partA('input.txt')}")

    print(f"Test value part B: {partB('test_input.txt')}")
    print(f"Answer part B: {partB('input.txt')}")

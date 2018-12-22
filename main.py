def possibilities(arr, i):
    if arr[i] is not None: return [arr[i]]

    this_row, this_col = i / 9, i % 9

    col_indicies = [x for x in range(81) if x % 9 == this_col]
    row_indicies = [x for x in range(81) if x // 9 == this_row]
    square_indicies = [x for x in range(81)
                       if (x % 9) // 3 == this_col // 3 and (x // 9) // 3 == this_row // 3]

    cant_be = set([arr[i] for i in col_indicies + row_indicies + square_indicies
                   if arr[i] in range(1, 10)])
    return list(set(range(1, 10)) - cant_be)

def solve(arr, i):
    if i >= 81: return arr
    orig = arr[i]
    for p in possibilities(arr, i):
        arr[i] = p
        soln = solve(arr, i + 1)
        if soln is not None: return soln
    arr[i] = orig
    return None

def pretty_print(arr):
    for i in range(9):
        for j in range(9):
            print arr[9*i + j],
        print

with open('data.txt', 'r') as f:
    content = f.read().replace('\n', '')
    arr = [None if ch == '.' else int(ch) for ch in content]

pretty_print(solve(arr, 0))

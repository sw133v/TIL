import sys

sys.stdin = open('2630input.txt', 'r')

def arrcopy(mat, r_range, c_range):
    lst = []
    for r in range(*r_range):
        r_lst = []
        for c in range(*c_range):
            r_lst += mat[r][c]
        lst += [r_lst]
    return lst

def check(int_a, lst):
    first_cor = lst[0][0]
    state = 0
    for r in range(int_a):
        for c in range(int_a):
            if first_cor != lst[r][c]:
                state = 1
                break
        if state == 1:
            break
    if state == 1:
        return False
    else:
        return True

def sol(int_a, lst):
    wnb = [0, 0]
    if int_a == [1]:
        if lst[0] == '1':
            return [0, 1]
        else:
            return [1, 0]

    if check(int_a, lst):
        if lst[0][0] == '1':
            return [0, 1]
        else:
            return [1, 0]

    rc_dict = {0: (0, int_a // 2), 1: (int_a // 2, int_a), }

    res = wnb
    for r in range(2):
        temp_lst = []

        for c in range(2):
            temp_lst = arrcopy(lst, rc_dict.get(r), rc_dict.get(c))
            wnb2 = sol(int_a // 2, temp_lst)
            res = [res[i] + wnb2[i] for i in range(2)]

    return res

int_a = int(input())
lst = [input().split() for _ in range(int_a)]
for val in sol(int_a, lst):
    print(val)

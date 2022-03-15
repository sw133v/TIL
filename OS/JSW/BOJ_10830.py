from copy import deepcopy

def transmat(mat):
    res = mat
    for r in range(len(mat)):
        for c in range(1+r, len(mat)):
            res[r][c], res[c][r] = res[c][r], res[r][c]
    return res

def my_sum(lst):
    res = 0
    for val in lst:
        res += val
    return res

def mat_mul(mat1, mat2):
    temp_mat = transmat(deepcopy(mat2))
    res = []
    for r in range(len(mat1)):
        temp_res = []
        for c in range(len(mat1)):
            temp = my_sum([mat1[r][i] * temp_mat[c][i] for i in range(len(mat1))])
            temp_res += [temp]
        res += [temp_res]
    return res

def matze(zisu, mat):
    if zisu == 1:
        return mat
    else:
        return mat_mul(matze((zisu // 2) + (zisu % 2), mat), matze(zisu // 2, mat))


len_jisu = list(map(int, input().split()))
mat = [list(map(int, input().split())) for _ in range(len_jisu[0])]
result = matze(len_jisu[1], mat)
for r in range(len_jisu[0]):
    for c in range(len_jisu[0]):
        print(result[r][c] % 1000, end=' ')
    print()


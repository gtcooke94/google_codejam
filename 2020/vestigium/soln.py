cases = int(input())
for case in range(1, cases + 1):
    repeated_rows = 0
    repeated_cols = 0
    mat_size = int(input())
    mat = [[] for _ in range(mat_size)]
    for row in range(mat_size):
        mat[row] = [int(i) for i in input().split()]

    trace = 0
    for d in range(mat_size):
        trace += mat[d][d]

    for r, row in enumerate(mat):
        rowset = set()
        for c, val in enumerate(row):
            if val in rowset:
                repeated_rows += 1
                break
            rowset.add(val)

    for c in range(mat_size):
        colset = set()
        for r in range(mat_size):
            val = mat[r][c]
            if val in colset:
                repeated_cols += 1
                break
            colset.add(val)
    print("Case #{}: {} {} {}".format(case, trace, repeated_rows, repeated_cols))

cases = int(input())
for case in range(1, cases + 1):
    inp = input()
    A = int(inp)
    B = 0
    for i, digit in enumerate(inp[::-1]):
        if digit == "4":
            A -= 10 ** i
            B += 10 ** i
    print("Case #{}: {} {}".format(case, A, B))

number_tests = int(input())
for t in range(1, number_tests + 1):
    maze_size = int(input())
    sequence = input()
    output = ["S" if s == "E" else "E" for s in sequence]
    print("Case #{}: {}".format(t, "".join(output)))

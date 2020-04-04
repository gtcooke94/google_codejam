# Idea:
# Keep track of num_open, num_closed. Open the number you need to before number, close number you need to before next number.

cases = int(input())
for case in range(1, cases + 1):
    digits = input()
    num_open = 0
    num_closed = 0
    final_str = ""
    for digit in digits:
        digit = int(digit)
        add_open = digit - num_open
        # add_open is positive, we have something like ...(, with 2, and need ....((2
        if add_open > 0:
            final_str += "(" * add_open
            num_open += add_open
        if add_open < 0:
            final_str += ")" * -add_open
            num_open += add_open
        final_str += str(digit)
        # add_open is neagtive, we have something like ...((((...., with 2, and need ...(((...))2

    # At the end, make sure parens are closed
    final_str += ")" * num_open
    print("Case #{}: {}".format(case, final_str))

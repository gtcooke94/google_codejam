import sys
import time
from copy import copy

output_file = open("temp.txt", "w")

inp = input()
cases, arr_size = (int(i) for i in inp.split())
print(cases, arr_size, file=output_file)

#  print(3)
#  sys.stdout.flush()
#  judge = input()
#  print(judge, file=output_file)
#  print(1111111111)
#  judge = input()
#  print(judge, file=output_file)


"""
Idea: go outside in

low starts at 0, high starts at end

"""


class Ind1Arr:
    def __init__(self, length):
        self.arr = [None] * length

    def __getitem__(self, i):
        return self.arr[i - 1]

    def __setitem__(self, i, val):
        self.arr[i - 1] = val

    def __len__(self):
        return len(self.arr)

    def compliment(self):
        self.arr = [int(not i) for i in self.arr]

    def reverse(self):
        self.arr = self.arr[::-1]

    def __eq__(self, o):
        return self.arr == o.arr

    def __str__(self):
        return str(self.arr)


def query(ind):
    print(ind)
    sys.stdout.flush()
    val = input()
    if val == "Y":
        sys.exit(1)
    elif val == "N":
        sys.exit(1)
    return int(val)


def solve(arr):
    arr = "".join(str(i) for i in arr.arr)
    print(arr)
    sys.stdout.flush()
    val = input()
    if val == "Y":
        return
    else:
        sys.exit(1)


def deduce_and_edit(arr, known_until):
    """
    25% of the time, the array is complemented: every 0 becomes a 1, and vice versa.
    25% of the time, the array is reversed: the first bit swaps with the last bit, the second bit swaps with the second-to-last bit, and so on.
    25% of the time, both of the things above (complementation and reversal) happen to the array. (Notice that the order in which they happen does not matter.)
    25% of the time, nothing happens to the array.
    """
    # If we get a match and a mismatch, we know which of the 4 cases. If we don't know a match and a mismatch, we can only get to 2 possible cases, but it doesn't matter because we both cases affect the things we know the same way
    low, high = 1, len(arr)
    lowval, highval = arr[low], arr[high]
    midlow, midhigh = None, None
    midlowval, midhighval = None, None

    # this query will initiate the flip
    new_low_val = query(low)
    match_inds = (None, None)
    mismatch_inds = (None, None)
    newmatch0, newmismatch0 = None, None

    if lowval == highval:
        # Go until we find a known mismatch or we don't know further
        match_inds = (low, high)
        newmatch0 = new_low_val
        for i in range(low + 1, known_until + 1):
            if arr[i] != arr[len(arr) + 1 - i]:
                midlow = i
                midhigh = len(arr) + 1 - i
                midlowval = arr[midlow]
                midhighval = arr[midhigh]
                mismatch_inds = (midlow, midhigh)
                break
    else:
        mismatch_inds = (low, high)
        newmismatch0 = new_low_val
        for i in range(low + 1, known_until + 1):
            if arr[i] == arr[len(arr) + 1 - i]:
                midlow = i
                midhigh = len(arr) + 1 - i
                midlowval = arr[midlow]
                midhighval = arr[midhigh]
                match_inds = (midlow, midhigh)
                break

    if not midlow:
        # We don't know exactly what happened, but it doesn't matter.
        if lowval == highval and lowval != newmatch0:
            # Only have matches
            # Case 1 or 3, compliment your array
            arr.compliment()
            # else Case 2 or 4, do nothing
        elif lowval != highval and lowval != newmismatch0:
            # Only have mismatches
            # Case 1 or 2, compliment your array
            arr.compliment()
            # else case 3 or 4, do nothing
        # Do an extra query to keep things consistent
        query(1)
        return 2

    #  print("120:", low, lowval, high, highval, midlow, midlowval, midhigh, midhighval, file=output_file)
    if midlow:
        # If  there is a match and a mismatch get the values
        if newmatch0 is not None:
            newmismatch0 = query(mismatch_inds[0])
        else:
            newmatch0 = query(match_inds[0])

        print("137: ", match_inds[0], newmatch0, mismatch_inds[0], newmismatch0, file=output_file)
            

        compliment = False
        reversal = False

        if arr[match_inds[0]] != newmatch0:
            # A compliment has to have happened
            compliment = True
            if arr[mismatch_inds[0]] == newmismatch0:
                # If a compliment happened, but the mismatch is still the same, a reversal happened as well
                reversal = True
        else:
            # A compliment did not happen
            if arr[mismatch_inds[0]] != newmismatch0:
                # A compliment did not happen, but the mismatch is different. A reversal happened
                reversal = True

        if compliment:
            arr.compliment()
        if reversal:
            arr.reverse()

    return 2


for case in range(1, cases + 1):
    arr = Ind1Arr(arr_size)
    known_until = 0
    query_count = 0
    # first query is "free"
    # don't use it for now
    for low in range(1, arr_size + 1):
        high = arr_size + 1 - low
        print(arr, file=output_file)
        print(low, high, query_count, file=output_file)
        arr[low] = query(low)
        arr[high] = query(high)
        known_until = low
        query_count = (query_count + 2) % 10
        if query_count == 0:
            # Things just changed, figure out what happened and fix it
            query_count = deduce_and_edit(arr, known_until)
        # We know the whole array
        if low >= high:
            break
    solve(arr)


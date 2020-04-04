cases = int(input())
#  cases = 1
for case in range(1, cases + 1):
    num_activities = int(input())
    #  num_activities = 3

    activities = []
    for i in range(num_activities):
        startendi = tuple((*(int(i) for i in input().split()), i))
        activities.append(startendi)
        #  print(activities)

    # Sort by start time
    # Greedy: Assign C first. If you can assign him to the next one, assign him. Otherwise assign J. If you can't assign either, break and IMPOSSIBLE
    activities = sorted(activities)
    cend = -1
    jend = -1
    final_list = ["0"] * num_activities
    final_str = None
    for start, end, activity_num in activities:
        #  print(start, end)
        #  import pdb; pdb.set_trace()
        if start < cend:
            if start < jend:
                final_str = "IMPOSSIBLE"
                break
        if start >= cend:
            cend = end
            final_list[activity_num] = "C"
        elif start >= jend:
            jend = end
            final_list[activity_num] = "J"

    if not final_str:
        final_str = "".join(final_list)

    print("Case #{}: {}".format(case, final_str))

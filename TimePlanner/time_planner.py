def time_planner(avA, avB, duration):
    for time in avA:
        for slot in avB:
            if time[0] >= slot[0] and time[0]+duration <= slot[1]:
                return [time[0], time[0]+duration]
            elif slot[0] >= time[0] and slot[0]+duration <= slot[1]:
                return [slot[0], slot[0]+duration]
    return[]


print(time_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8))
# expect [60,68]

print(time_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 72]], 12))
# expect [60,72]

print(time_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12))
# expect []

# runtime efficient: O(n*m)

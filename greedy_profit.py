"""schedule"""
def binary_search(jobs, start_index):
    """Find the most recent job that doesn't conflict with the job at start_index."""
    low, high = 0, start_index - 1
    while low <= high:
        mid = (low + high) // 2
        if jobs[mid][1] <= jobs[start_index][0]:
            if jobs[mid + 1][1] <= jobs[start_index][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1

def schedule():
    """schedule function"""
    length = int(input())
    jobs = []
    for _ in range(length):
        jobs.append(list(map(int, input().split())))
    jobs.sort(key=lambda x: x[1])
    length = len(jobs)
    dynamic_programming = [0 for _ in range(length)]
    dynamic_programming[0] = jobs[0][2]

    for i in range(1, length):
        # Find profit including the current job
        incl_prof = jobs[i][2]
        l = binary_search(jobs, i)
        if l != -1:
            incl_prof += dynamic_programming[l]

        # Store maximum of including and excluding
        dynamic_programming[i] = max(incl_prof, dynamic_programming[i - 1])

    return dynamic_programming[length-1]  # Return maximum profit

print(schedule())  # prints 250

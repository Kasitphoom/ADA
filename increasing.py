"""Increasing Subsequence"""
memorization = {}

"""Increasing recursive function to find increasing sequences"""
def increasing(k):

    if k in memorization:
        return memorization[k]

    if k == 0:
        return 1

    max_length = 0
    for i in range(k):
        if sample[i] <= sample[k]:
            val = increasing(i)
            if max_length < val:
                max_length = val
    memorization[k] = 1 + max_length
    return memorization[k]

def lis():
    max_length = 0
    for i in range(len(sample)):
        val = increasing(i)
        if val > max_length:
            max_length = val
    return max_length

sample = list(map(int, input().split()))
print(lis())

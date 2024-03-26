"""Finding max value from inequality"""
MAX_VALUE = int(input())

"""Function finding the max value using binary search"""
def opt():
    half = 0
    left = 0
    right = MAX_VALUE

    while left <= right:
        half = (left + right) // 2
        if half * half + half <= MAX_VALUE:
            left = half + 1
        else:
            right = half - 1

    print(right)

opt()

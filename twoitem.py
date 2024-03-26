"""Two Item finding"""
"""Function of finding sum of two numbers"""
def opt():
    target = int(input())
    arr = list(map(int, input().split()))

    arr = sorted(arr)
    low = 0
    high = len(arr) - 1

    while low != high:
        calc = arr[low] + arr[high]
        if calc == target:
            return "Yes"
        elif calc < target:
            low += 1
        else:
            high -= 1

    return "No"

print(opt())

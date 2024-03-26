"""Finding subset sum problem"""
mem = {}

"""Finding that is there a target in the set"""
def check(index, target):
    if (index, target) in mem:
        return mem[(index, target)]

    if index == 0:
        mem[(index, target)] = (target == 0)
        return (target == 0)

    if target < inputSet[index - 1]:
        mem[(index, target)] = check(index - 1, target)
        return mem[(index, target)]
    else:
        mem[(index, target)] = check(index - 1, target) or check(index - 1, target - inputSet[index - 1])
        return mem[(index, target)]

inputSet = list(map(int, input().split()))
target = int(input())
print(check(len(inputSet), target))

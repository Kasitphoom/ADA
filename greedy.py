"""greedy programming"""
def greedy():
    """greedy function"""
    length = int(input())
    works = []
    for _ in range(length):
        works.append(list(map(int, input().split())))
    works.sort(key=lambda x: x[1])
    time = works[0][1]
    count = 1
    for work in works[1:]:
        if work[0] >= time:
            time = work[1]
            count += 1
    print(count)

greedy()

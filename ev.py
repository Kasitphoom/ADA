def ev():
    dest = int(input())
    stations = input()
    lastLine = input()

    if lastLine != "$":
        return

    if stations == "":
        return dest

    stations = stations.split(' ')
    stations = list(map(int, stations))
    stations.extend([dest])

    maxLen = 0

    for i in range(0, len(stations) - 1):
        diff = stations[i + 1] - stations[i]
        if diff > maxLen:
            maxLen = diff

    result = maxLen
    lenSum = 0

    for i in range(0, len(stations) - 1):
        if i == 0:
            if abs(maxLen - stations[i]) <= abs(stations[i + 1] - stations[i]):
                result += 1
                maxLen -= 1
            lenSum = maxLen
            continue

        if lenSum - (stations[i + 1] - stations[i]) > 0:
            lenSum -= (stations[i + 1] - stations[i])
        else:
            result += 1
            maxLen -= 1
            lenSum = maxLen

    return result

print(ev())

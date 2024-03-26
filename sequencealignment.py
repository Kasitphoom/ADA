"""Sequence alignment"""
STR1 = input()
STR2 = input()
def opt(string1, string2):
    """find shortest replacement sequence"""
    if len(string2) == 0:
        return len(string1)

    if len(string1) == 0:
        return len(string2)

    if string1[-1] == string2[-1]:
        return opt(string1[:-1], string2[:-1])
    else:
        return min(
            opt(string1[:-1], string2[:-1]),
            opt(string1[:-1], string2),
            opt(string1, string2[:-1])
        ) + 1

print(opt(STR1, STR2))

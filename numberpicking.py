"""Number Picking method"""

"""calling numberPicking for both side"""
def opt():
    arr = list(map(int, input().split()))
    if len(arr) == 0:
        return True
    return number_picking(arr[1:], arr[0]) or number_picking(arr[:-1], arr[-1])

"""find way to win the game"""
def number_picking(arr, picked_number):
    if len(arr) == 0:
        return True

    pick_left = False
    pick_right = False

    if abs(picked_number - arr[0]) <= 9:
        pick_left = number_picking(arr[1:], arr[0])
    if abs(picked_number - arr[-1]) <= 9:
        pick_right = number_picking(arr[:-1], arr[-1])

    return pick_left or pick_right

print("Yes" if opt() else "No")

#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)

    unlocked = [False] * n

    unlocked[0] = True

    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)

#!/usr/bin/python3
"""Déterminer si toutes les boites d'une liste peuvent être ouvertes"""


def canUnlockAll(boxes):
    n = len(boxes)

    unlocked = {0}

    keys = list(boxes[0])

    while keys:
        current_key = keys.pop()
        if current_key < n and current_key not in unlocked:
            unlocked.add(current_key)
            keys.extend(boxes[current_key])

    return len(unlocked) == n

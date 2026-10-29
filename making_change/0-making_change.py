#!/usr/bin/python3
"""
Module de résolution du problème de monnaie (making change).
"""


def makeChange(coins, total):
    """Calcule le nombre minimal de pièces nécessaires
    pour obtenir un total donné en utilisant
    la programmation dynamique.

    Args:
        coins (list of int): La liste des valeurs des pièces.
        total (int): Le montant total à atteindre.

    Returns:
        int: Le nombre minimal de pièces, ou -1 si
             impossible, ou 0 si le total <= 0.
    """
    if total <= 0:
        return 0

    # Tableau pour stocker le nombre minimal de pièces
    # On initialise avec une valeur infini
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

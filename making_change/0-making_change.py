#!/usr/bin/python3
"""
Module de résolution du problème de monnaie (making change).
"""

def makeChange(coins, total):
    """Calcule le nombre minimal de pièces nécessaires pour obtenir un total donné
    en utilisant la programmation dynamique.

    Args:
        coins (list of int): La liste des valeurs des pièces disponibles.
        total (int): Le montant total à atteindre.

    Returns:
        int: Le nombre minimal de pièces nécessaires, ou -1 s'il est impossible
             d'atteindre le total, ou 0 si le total est inférieur ou égal à 0.
    """
    if total <= 0:
        return 0

    # Tableau pour stocker le nombre minimal de pièces pour chaque montant de 0 à total
    # On initialise avec une valeur infini (représentée ici par total + 1)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

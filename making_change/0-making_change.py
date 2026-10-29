#!/usr/bin/python3
"""
Module de résolution du problème de monnaie (making change).
"""

def makeChange(coins, total):
    """Calcule le nombre minimal de pièces nécessaires pour obtenir un total donné
    en utilisant une approche gloutonne (greedy).

    Note : L'approche gloutonne ne garantit pas toujours la solution optimale
    pour tous les systèmes de monnaie, mais elle fonctionne pour les monnaies standard.

    Args:
        coins (list of int): La liste des valeurs des pièces disponibles.
        total (int): Le montant total à atteindre.

    Returns:
        int: Le nombre minimal de pièces nécessaires, ou -1 s'il est impossible
             d'atteindre le total, ou 0 si le total est inférieur ou égal à 0.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_count = 0

    for coin in coins:
        if total <= 0:
            break

        coin_count += total // coin
        total = total % coin

    if total != 0:
        return -1

    return coin_count

#!/usr/bin/python3
"""Module to determine the winner of a prime number game.
"""

def isWinner(x, nums):
    """Determines the winner of a prime number game played over `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # Generate primes up to the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # Count the primes less than each number in nums for each round
    for _, n in zip(range(x), nums):
        primes_counter = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_counter % 2 == 0
        marias_wins += primes_counter % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
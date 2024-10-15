#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(rounds, numbers):
    """
    Determines the winner of a series of prime number removal games.

    Args:
        rounds (int): The number of rounds to be played.
        numbers (list of int): A list of integers where each integer n denotes
        a set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.

    Raises:
        None.
    """
    # Check for invalid input
    if rounds <= 0 or numbers is None:
        return None
    if rounds != len(numbers):
        return None

    # Initialize scores for both players
    score_ben = 0
    score_maria = 0

    # Create a list 'primes' of length sorted(numbers)[-1] + 1
    # with all elements initialized to 1
    primes = [1 for _ in range(sorted(numbers)[-1] + 1)]
    # The first two elements of the list, primes[0] and primes[1], are set to 0
    # because 0 and 1 are not prime numbers
    primes[0], primes[1] = 0, 0

    # Use the Sieve of Eratosthenes algorithm to generate
    # an array of prime numbers
    for index in range(2, len(primes)):
        eliminate_multiples(primes, index)

    # Play each round of the game
    for n in numbers:
        # If the sum of prime numbers in the set is even, Ben wins
        if sum(primes[0:n + 1]) % 2 == 0:
            score_ben += 1
        else:
            score_maria += 1

    # Determine the winner of the game
    if score_ben > score_maria:
        return "Ben"
    if score_maria > score_ben:
        return "Maria"
    return None


def eliminate_multiples(prime_list, prime_number):
    """
    Removes multiples of a prime number from an array of potential prime
    numbers.

    Args:
        prime_list (list of int): An array of potential prime numbers.
        prime_number (int): The prime number to remove multiples of.

    Returns:
        None.

    Raises:
        None.
    """
    # This loop iterates over multiples of a prime number
    # and marks them as non-prime by setting their corresponding
    # value to 0 in the input list prime_list.
    # Starting from 2, it sets every multiple of prime_number
    # up to the length of prime_list to 0.
    # If the index i * prime_number is out of range for the
    # list prime_list, the try block will raise an IndexError exception,
    # and the loop will terminate using the break statement.
    for i in range(2, len(prime_list)):
        try:
            prime_list[i * prime_number] = 0
        except (ValueError, IndexError):
            break

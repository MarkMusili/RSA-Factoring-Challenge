#!/usr/bin/python3

def factorize(n):
    factors = []
    q = 2

    while q <= n:
        if n % q == 0:
            p = n // q
            factors.append((p, q))
            break
        q += 1

    return factors





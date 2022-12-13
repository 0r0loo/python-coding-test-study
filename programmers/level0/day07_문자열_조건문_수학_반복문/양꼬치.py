def solution(n, k):
    gogi = n * 12000
    drink = k * 2000

    if n > 9:
        drink -= 2000 * (n // 10)

    return gogi + drink
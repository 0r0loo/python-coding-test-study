def solution(n):
    answer = n // 7 + ( 0 if n % 7 == 0 else 1)
    return answer
def solution(n):
    answer = 1
    six_multiple = 6

    while (6 * answer) % n:
        answer += 1

    return answer
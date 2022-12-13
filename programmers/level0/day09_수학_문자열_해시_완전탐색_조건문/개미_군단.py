def solution(hp):
    answer = 0
    #     5, 3, 1

    answer += hp // 5

    rest = hp % 5

    answer += rest // 3

    rest = rest % 3

    answer += rest // 1

    return answer
def solution(my_string, n):
    answer = ''

    for index in range(len(my_string)):
        answer += my_string[index] * n

    return answer
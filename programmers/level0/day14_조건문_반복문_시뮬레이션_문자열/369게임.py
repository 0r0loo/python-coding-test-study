def solution(order):
    answer = 0
    clap_list = ['3', '6', '9']

    for char in str(order):
        if char in clap_list:
            answer += 1

    return answer
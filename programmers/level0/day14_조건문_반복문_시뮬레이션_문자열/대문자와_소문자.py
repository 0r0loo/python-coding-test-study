def solution(my_string):
    answer = ''

    for cha in my_string:
        if cha.isupper():
            answer += cha.lower()
        else:
            answer += cha.upper()

    return answer
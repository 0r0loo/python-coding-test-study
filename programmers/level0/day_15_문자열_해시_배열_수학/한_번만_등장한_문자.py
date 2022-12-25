def solution(s):
    answer = ''

    arr = list(s)

    for i in arr:
        if arr.count(i) == 1:
            answer += i

    return ''.join(cha for cha in sorted(list(answer)))


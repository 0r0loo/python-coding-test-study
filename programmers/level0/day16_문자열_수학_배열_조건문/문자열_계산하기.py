def solution(my_string):
    answer = 0
    arr = my_string.split(' ')

    answer += int(arr[0])

    for i in range(1, len(arr)):
        if arr[i] == "+":
            answer += int(arr[i + 1])
        if arr[i] == '-':
            answer -= int(arr[i + 1])

    return answer
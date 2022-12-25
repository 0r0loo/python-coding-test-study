def solution(array, n):
    answer = 0
    temp = float("inf")
    array.sort(reverse=True)

    for i in array:
        if abs(n - i) <= temp:
            answer = i
            temp = abs(n - i)

    return answer
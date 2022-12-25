def solution(array):
    max_num = max(array)

    index = array.index(max_num)

    answer = [max_num, index]

    return answer
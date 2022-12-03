def solution(array):
    answer = [0, 0]
    dit = {}

    for num in array:
        if not num in dit:
            dit[num] = 0
        dit[num] += 1

        if dit[num] > answer[1]:
            answer = [num, dit[num]]

    max_num = max(list(dit.values()))
    values = list(dit.values())

    if values.count(max_num) == 1:
        idx = values.index(max_num)
        return list(dit.keys())[idx]
    else:
        return -1

print(solution([1, 2, 3, 3, 3, 4]))
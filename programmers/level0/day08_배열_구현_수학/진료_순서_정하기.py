def solution(emergency):
    length = len(emergency)
    list = [0 for i in range(length)]

    for i in range(length):
        for j in range(length):
            if emergency[j] >= emergency[i]:
                list[i] += 1

    return list
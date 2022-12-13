def solution(num_list, n):
    answer = [[]]

    def list_chuck(arr, n):
        return [arr[i: i + n] for i in range(0, len(arr), n)]

    return list_chuck(num_list, n)
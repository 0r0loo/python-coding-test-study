def solution(numbers):
    def multi_two(num):
        return 2 * num

    return list(map(multi_two, numbers))

def solution(numbers):
    return list(map(lambda x: x * 2, numbers))


def solution(numbers):
    return [num*2 for num in numbers]
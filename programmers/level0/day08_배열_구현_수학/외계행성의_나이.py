def solution(age):
    list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    result = ''
    str_age = str(age)

    for cha in str_age:
        result += list[int(cha)]

    return result
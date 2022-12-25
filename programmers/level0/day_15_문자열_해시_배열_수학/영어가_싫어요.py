def solution(numbers):
    answer = ""
    arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    temp = ""
    for char in numbers:
        temp += char
        if temp in arr:
            answer += str(arr.index(temp))
            temp = ""

    return int(answer)
def solution(rsp):
    answer = ''

    def win(rsp):
        if rsp == "0":
            return "5"
        if rsp == "2":
            return "0"
        if rsp == "5":
            return "2"

    for cha in rsp:
        answer += win(cha)

    return answer
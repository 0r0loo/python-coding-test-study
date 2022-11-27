import math

def solution(denum1, num1, denum2, num2):
    answer = []
    denum1 *= num2
    denum2 *= num1
    num3 = num1 * num2
    n = math.gcd(denum1 + denum2, num3)
    if n == 1:
        answer.append(denum1 + denum2)
        answer.append(num3)
    else:
        answer.append((denum1 + denum2) / n)
        answer.append(num3 / n)


    return answer



# 051 리스트 생성
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']

# 052 리스트에 원소 추가
movie_rank.append('배트맨')

# 053
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 55
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
movie_rank.pop()
movie_rank.pop()
print(movie_rank)

# 답
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

print(lang1 + lang2)


# 057
nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums))
print(min(nums))

# 058
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 060
nums = [1, 2, 3, 4, 5]
print(sum(nums) / len(nums))

# 061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])


# 62
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 63
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# 64
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 65
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0])
print(interest[2])

# 066 join 메서드
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

# 067 join 메서드


# 069 문자열 split 메서드
string = "삼성전자/LG전자/Naver"
print(string.split("/"))

# 070 리스트 정렬
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

data = [2, 4, 3, 1, 5, 10, 9]
data2 = sorted(data)
print(data2)

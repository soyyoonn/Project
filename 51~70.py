#51번
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

#52번
movie_rank.append("배트맨")
print(movie_rank)

#53번
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

#54번
del movie_rank[3]
print(movie_rank)

#55번
del movie_rank[2:]
print(movie_rank)

#56번
lang1 = ["c", "c++", "java"]
lang2 = ["python", "go", "c#"]
print(lang1+lang2)

#57번
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ",max(nums))
print("min: ",min(nums))

#58번
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#59번
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

#60번
nums = [1, 2, 3, 4, 5]
print(sum(nums)//5)

#61번
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#62번
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#63번
print(nums[1::2])

#64번
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#65번
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

#66번
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(' '.join(interest))

#67번
print('/'.join(interest))

#68번
print('\n'.join(interest))

#69번
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

#70번
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)





#반복문 (for)
"""
for 변수 in 반복할 대상:
    반복할 코드
"""
#리스트 순회
fruits = ["사과", "바나나", "딸기", "포도"] # fruits - for문 밖에서 쓸 수 있음 (전역변수)

for fruit in fruits:
    print(fruit) # fruit - 여기 for문 안 에서만 쓸수 있음 (지역변수)

#딕셔너리 순회
scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
for key in scores: #key를 빼와서 변수에 할당
    print(key, "의 점수는", scores[key])

#튜플 순회
a_tuple = ("안녕", "하세요", "반갑습니다")
for a in a_tuple:
    print(a)

#세트 순회
a_set = {"사과", "바나나", "체리", "딸기", "오렌지"}
sorted_a_list = sorted(a_set)
for a in sorted_a_list:
    print(a)

#세트 정렬 추가 설명
numbers = {3, 1, 4, 1, 5, 9, 2}
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(type(sorted_numbers))



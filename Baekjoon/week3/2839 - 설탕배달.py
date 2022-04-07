# def sugar_nums(sugar):
#     count_five = 0
#     count_three = 0
#     if sugar % 5 == 0:
#         count_five += sugar // 5
#     else:
#         count_five += sugar // 5
#         if (sugar % 5) % 3 == 0:
#             count_three = (sugar % 5) // 3
#         else:
#             count_five = 0
#             count_three = -1
#     result = count_five + count_three
    
#     return print(result) 

# sugar = int(input())
# sugar_nums(sugar)

# --------------------------------------

sugar = int(input())    # 설탕 무게 입력

pack_num = 0        # 포장지 개수 변수

while sugar > 0:    # 설탕이 0보다 작아질때 까지 반복
    if sugar % 5 == 0:  # 5로 나누어 떨어지면
        pack_num += (sugar // 5)    # 그 배수만큼 포장지 수에 넣고 
        break   # 반복문 끝냄
    sugar -= 3  # sugar양을 3씩 뺌
    pack_num += 1   # 3씩 뺀 만큼 포장지 횟수는 1개씩 늘어남

if sugar < 0:   # 0보다 작으면 마지막에 3이나 5로 안나누어 떨어진것이니까 -1 출력
    print(-1)
else:           # 0보다 크면 아직 반복문에 있을 것이고 0이면 나누어 떨어진 것 이므로 그때는 포장지 수 출력
    print(pack_num)


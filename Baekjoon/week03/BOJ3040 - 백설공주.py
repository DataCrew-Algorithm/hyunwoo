# def real_little(lst):
#     global exact
#     union_nums = sum(lst)
#     for i in range(len(lst) - 1):
#         for j in range(i+1, len(lst)-1):
#             if union_nums - (lst[i] + lst[j]) == 100:
#                 # lst.pop(i)
#                 # lst.pop(j-1)  
#                 first = i
#                 second = j
#                 exact = True
#                 break
        
#         if exact:
#             break

#     return first, second

# little = []
# new_little = []
# exact = False
# fir = 0
# sec = 0


# for _ in range(9):
#     little_num = int(input())
#     little.append(little_num)

# union_nums = sum(little)
# # print(little)
# # print(union_nums)
# remove_nums = 0
# for i in range(len(little) - 1):
#     for j in range(i+1, len(little)-1):
#         remove_nums = little[i] + little[j]
#         if union_nums - remove_nums == 100:
#             fir = i
#             sec = j
#             exact = True
#             break
 
#     if exact:
#         break

# for i in range(len(little)):
#     if little[i] == little[fir]:
#         continue
#     elif little[i] == little[sec]:
#         continue
#     else:
#         new_little.append(little[i])

# print(new_little)


# ----------------------------------------------------------------------------
little = []     # 9난쟁이의 숫자를 받을 리스트
new_little = [] # 진짜 7난쟁이의 숫자를 받을 리스트
complete = False    # flag 생성

for i in range(9):
    nums = int(input())
    little.append(nums) # 9난쟁이의 숫자를 받아 리스트 형성

little_sum = sum(little)    # 리스트 총 합을 구해서 변수 지정

for i in range(len(little)-1):  # 아래 for문과 함께 2개씩 짝지어 리스트 안에 요소들을 고르기 위해 for문 돌림
    for j in range(i+1, len(little)):
        if little_sum - (little[i] + little[j]) == 100:     # 합에 리스트 요소 2개를 뺏을때 100이 된다면
            fir_idx = i         # 1번째 가짜 난쟁이 요소 인덱스값 변수 지정
            sec_idx = j         # 2번째 가짜 난쟁이 요소 인덱스값 변수 지정
            complete = True     # flag 값 True로 재설정        
            for x in range(len(little)):    # 반복문 돌려 진짜 7난쟁이의 숫자만 넣음
                if x == fir_idx:
                    continue
                elif x == sec_idx:
                    continue
                else:
                    new_little.append(little[x])    # 가짜 난쟁이의 인덱스 값을 만나면 continue로 무시하고 진짜 난쟁이 인덱스 값을 만났을 때만 append시켜줌 
            break
    if complete:    # flag 위에 수행을 다 했기 때문에 반복문 더 돌 필요 없어서 break 
        break

for _ in new_little:
    print(_)    # 새로 형성한 리스트 출력


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] + a[j] == 10:
#             first = i
#             second = j
#             print(f"({first}, {second})")
     
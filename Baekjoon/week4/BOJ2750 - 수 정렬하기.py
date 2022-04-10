# nums = int(input())
# num = [int(input()) for i in range(nums)]
# num_1 = 0
# num_2 = 0

# while sorted(num) != num:
#     for j in range(nums-1):
#         num_1 = num[j]
#         num_2 = num[j+1]
#         if num_1 > num_2:
#             num[j] = num_2
#             num[j+1] = num_1
#         else:
#             continue


# for _ in num:
#     print(_)
        

# ------------------------------------------------------------------

nums = int(input())         # 받을 숫자 개수
num = [int(input()) for i in range(nums)]       # 받은 숫자를 리스트로 만듬
num_1 = 0       # 2개의 숫자 비교를 위해 변수 2개 만듬
num_2 = 0        

for i in range(nums):       # 받은 숫자 개수 만큼 반복문 돌림
    for j in range(nums-1): # j번째 수와 j + 1번째 수를 비교하기 위해 nums - 1만큼 반복 돌림
        num_1 = num[j]      
        num_2 = num[j+1]
        if num_1 > num_2:   # num_1이 num_2보다 크다면
            num[j] = num_2
            num[j+1] = num_1    # 위치를 바꿔줌
        else:
            continue        # 아니라면 다시 반복문 수행


for _ in num:
    print(_)

# 버블 정렬   
 
  
# ------------------------------------------------------------------


nums = int(input())     # 받을 숫자 개수
num = [int(input()) for i in range(nums)]   # 받은 숫자를 리스트로 만듬
sort_num = []       # 정렬시키기 위해 새로운 리스트를 만듬

for i in range(nums):       # 받은 숫자 갯수 만큼 반복문 돌림 
    min_num = min(num)      # 받은 숫자 중 제일 최소값 저장하는 변수로 저장
    min_idx = num.index(min_num)    # 최소값 인덱스 값도 변수로 저장
    sort_num.append(min_num)    # 새로운 리스트에 최소값을 넣어줌
    num.pop(min_idx)            # 최소값을 기존 리스트에서 제외 시켜줌

for _ in sort_num:      # 출력
    print(_)


# 선택 정렬
# ------------------------------------------------------------------

e, f, c = map(int, input().split())

bottle_num = e + f  # 현재 가지고 있는 빈병 
soda_num = 0        # 먹은 탄산음료 총 합 
soda = 0            # 빈병을 가지고 먹을 수 있는 탄산음료 수

while bottle_num >= c:  # 빈병이 바꿔야 되는 병 수보다 같거나 클때만 반복문 실행
    soda = bottle_num // c  # 1회 먹을 수 있는 새 탄산 음료
    soda_num += soda        # 탄산음료 총 합에다 더 해줌
    bottle_num += soda - (soda * c)     # 새 탄산음료를 먹으면 또 빈병이 나오므로 그 수와 soda에 c를 곱해준 수의 차이를 빈병에 더해줌
    
print(soda_num)     # 먹은 총수 출력





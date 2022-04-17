lst = []	# 1000개의 숫자를 받을 리스트 생성
answer = 0	# 출력할 정답값 

for i in range(1, 46):	# A, B가 1000개 이하이므로 비슷한 45까지 리스트에 넣음
    lst_sub = [i]*i		# 해당 숫자를 그 숫자만큼 곱 
    lst += lst_sub		# 리스트에 더해줌

A, B = map(int, input().split())	# A, B값 받음

for j in range(A, B+1):	# A,B값을 이용해 숫자 구함
    answer += lst[j-1]

print(answer)		# 정답 출력
test = int(input())     # 테스트 할 횟수 입력받음

for i in range(test):
    quiz = input()          # 퀴즈의 결과를 받음
    result = len(quiz)      # 퀴즈의 결과 만큼 반복문을 돌리기 위해 변수 설정
    count = 0               # 연속으로 맞추는 경우 하나씩 숫자를 올리기 위해 변수 생성
    ans_sum = 0             # 총 점수 계산을 위한 변수 생성

    for j in range(result):
        if quiz[j] == "O":   
            count += 1          # 맞췄을 경우 count를 1 올려줌
            ans_sum += count    # count의 결과를 ans_sum에 더해줌
        elif quiz[j] == "X":
            count = 0           # 못 맞췄을 경우 다시 count를 0으로 초기화

    print(ans_sum)
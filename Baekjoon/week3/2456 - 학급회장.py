# def vote_max(temp):
#     vote_sum = []
#     # count_1_1 = 0
#     # count_1_2 = 0
#     # count_1_3 = 0
#     # count_2_1 = 0
#     # count_2_2 = 0
#     # count_2_3 = 0
#     # count_3_1 = 0
#     # count_3_2 = 0
#     # count_3_3 = 0

#     # vote_dict = {'1-1' : 0, '1-2' : 0, '1-3' : 0, '2-1' : 0, '2-2' : 0,
#     #            '2-3' : 0, '3-1' : 0, '3-2' : 0, '3-3' : 0}
#     for i in range(temp):
#         vote = list(map(int, input().split()))
#         vote_sum += vote

#     per_num = vote_sum.index(max(vote_sum))
#     vote_rate = max(vote_sum)

#     return per_num, vote_rate


# def equal_vote(vote_sum):
#     if  vote_sum.count(max(vote_sum)) >= 2:



N = int(input())

scores = [0] * 3

score = [0] * 3

for n in range(N):
    one, two, three = map(int, input().split())
    scores[0] += one
    scores[1] += two
    scores[2] += three

    score[0] += one * one
    score[1] += two * two
    score[2] += three * three

max_score = max(scores)
chk = 0
for i in range(3):
    if scores[i] == max_score:
        chk += 1

if chk == 1:
    for i in range(3):
        if max_score == scores[i]:
            print(i+1, scores[i])
            break
else:
    chk_max_score = max(score)
    cnt = 0
    lst = []
    for i in range(3):
        if score[i] == chk_max_score:
            cnt += 1
            lst.append(i)

    if cnt > 1:
        print(0, scores[lst[0]])
    else:
        print(lst[0]+1, scores[lst[0]])

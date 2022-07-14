# 실패
# 예시로 나온 숫자만 생각을 함
# 함수에 for if 좀 더 생각해보기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = list(map(int, input().split()))
graph = [[0]*n for i in range(n)]
visited = [[0]*n for i in range(n)]
ans = []

def floyd():
    for _ in range(n):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    if graph[i][j] == 1:
                        visited[i][j] = 1
                    if (graph[i][k] == 1 and graph[k][j] == 1):
                        visited[i][j] = 2
                    if (graph[i][k] == 1 and graph[k][_] == 1 and graph[_][j] == 1):
                        visited[i][j] = 3


for i in range(m):
    a, b = list(map(int, input().split()))
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

floyd()

for i in visited:
    ans.append(sum(i))

print(ans.index(min(ans)) + 1)

# =======================================================================================
# 블로그
# 플로이드 워셜

import sys
from collections import deque
input = sys.stdin.readline
Min = 1000000000
n,m = map(int,input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for i in range(n): #거치는점
    for j in range(n): #출발점
        for k in range(n): #도착점
            if j == k:
                continue
            elif graph[j][i] and graph[i][k]:
                if graph[j][k] == 0:
                    graph[j][k] = graph[j][i] + graph[i][k]
                else:
                    graph[j][k] = min(graph[j][k],graph[j][i] + graph[i][k])
for i in range(n):
    result = 0
    for j in range(n):
        result += graph[i][j]
    if Min > result:
        Min = result
        person = i
print(person+1)


# =======================================================================================
# 블로그
# bfs

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph,start):
    num = [0] * (n+1)
    q = deque()
    visited[start] = 1
    q.append(start)
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                num[i] = num[a]+1
                q.append(i)
                visited[i] = 1
    return sum(num)

result = []
for i in range(1,n+1):
    visited = [0 for _ in range(n+1)]
    result.append(bfs(graph,i))
print(result.index(min(result))+1)
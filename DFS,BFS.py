#DFS/BFS
def recursive_function(i):
#100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서' , i + 1, '번째 재귀함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)

#팩토리얼 구현 예제

#반복적으로 구현할 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

#재귀적으로 구현할 n!
def factorial_recursive(n):
    if n <= 1: #n이 1이하인 경우 1을 반환
        return 1
    # n! = n * (n-1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

#각각의 방식으로 구현한 n! 출력 (n=5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))


#DFS 소스코드 예제
#DFS 매서드 정의
def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
#각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

#정의된 DFS 함수 호출
dfs(graph,1,visited)

#BFS
#BFS 소스코드 예제 

from collections import deque


#BFS 매서드 정의
def bfs(graph,start,visited):
    #큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue:
    #큐에서 하나의 원소를 뽑아 출력하기
         v = queue.popleft()
         print(v, end=' ')
         #아직 방문하지 않은 인접한 원소들을 큐에 삽입
         for i in graph[v]:
             if not visited[i]:
                 queue.append(i)
                 visited[i] = True

#각 노드가 연결된 정보를 표현(2차원리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9 

#정의된 BFS 함수 호출
bfs(graph,1,visited)

#음료수 얼려먹기 : 문제 해결 아이디어

#DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하 , 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1,y)
        dfs(x,y - 1)
        dfs(x + 1, y)
        dfs(x,y + 1)
        return True
    return False

#N,M을 공백을 기준으로 구분하여 입력 받기
n , m = map(int, input().split())

#2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1
print(result) #정답 출력


#미로 탈출
# N, M을 공백으로 기준으로 구분하여 입력 받기
n , m = map(int,input().split())
#2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#이동할 네 가지 방향 정희 (상,하,좌,우)
dx = [-1 , 1,0,0]
dy = [0,0,-1,1]

#BFS 소스코드 구현
def bfs(x,y):
    #큐(Queue) 구현을 위해 deque 라이브러리 사용
   queue = deque()
   queue.append((x, y))
    # 큐가 빌 때까지 반복하기
   while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
        return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))
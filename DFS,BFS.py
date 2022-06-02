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
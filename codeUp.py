#모험가 길드
n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data: #공포도를 낮은 것부터 하나씩 확인하여
    count += 1 #현재 그룹에 해당 모험가를 포함시키기
    if count >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 #총 그룹의 수 증가시키기
        count = 0 #현재 그룹에 포함된 모험가의 수 초기화

# print(result) #총 그룹의 수 출력


# 구현 : 시물레이션과 완전 탐색 

for i in range(5):
    for j in range(5):
        print('(', i , ',' , j ,')', end= ' ')
    print()


#상하좌우 : 문제 설명

# N 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L , R , U , D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        #공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
            #이동 수행
        x , y = nx,ny

print(x,y)

#시각

h = int(input())

count =  0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에서 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)

#왕실의 나이트
#현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

#나이트가 이동할 수 있는 8가지 방향 정의 
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    #해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)


#문자열 재정렬ㅇ
#정렬이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것
#일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용된다.

#선택정렬 소스코드

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i #가장 작은 원소의 인덱스
    for j in range (i+1 ,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #스와프

print(array)

#삽입 정렬 소스코드



#연습문제 제곱
data = int(input())
print(data * data)


#while문 연습문제
num = int(input())

int = 0
while int <= num:
    print(num)
    int += 1

#while문 제곱
num = int(input())

int = 1
while int <= num:
    print(int, int*int)
    int += 1


# if-elif-else 연습문제

num = int(input())
result = str(num)

if num >= 1000:
    result = str(num // 1000) + 'k'
elif num >= 0:
    pass

print(result)

num = int(input())
result = str(num)

if num >= 1000000:
    result = str(num // 1000000) + 'M'
elif num >= 0:
    pass

print(result)

# 양수만 덧셈하기
sum = 0
while True:
    num = int(input())
    if num < 0:
        break
    else:
        sum += num

print(sum)


# 윤년 판별하기
year = int(input())

if year%4 != 0:
    print("평년")
elif year%100 != 0:
    print("윤년")
elif year%400 != 0:
    print("평년")
else: 
    print("윤년")

#for문

famliy = ['mom' , 'father', 'jsy', 'jhy','me']

for x in famliy:
    print(x , len(x))  
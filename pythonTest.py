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
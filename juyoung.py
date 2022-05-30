import imp


import time
start_time = time.time() #측정 시작

#프로그램 소스코드
end_time = time.time() #측정종료
print("time "  , end_time - start_time) #수행시간출력

#파이썬 자료형 : 정수형 , 실수형, 복소수형, 문자열, 리스트 , 튜플 , 사전
# 정수형 : 양의 정수, 음의 정수, 0 포함
# 실수형 : 소수점 아래의 데이터를 포함하는 수 자료형

# 지수 표현 방식 
# 파이썬에서는 e나 E를 이용한 지수 표현 방식을 이용 가능.


a = 1e9
print(a)
a = int(1e9)
print(a)

a = 75.25e1
print(a)

a = 3954e-3
print(a)

# 2진수 체계에서 실수는 정확성이 떨어짐.
a = 0.3 + 0.9
print(a)

if a == 0.9 :
  print(True)
else :
  print(False)

  #false

  # 개발 과정에서 실수 값을 제대로 비교하지 못해서 원하는 결과를 얻지 못할 수 있다.
  # -> 이럴 때 round() 함수 이용가능.

a = 0.3 + 0.9
print(round(a,4))

#수 자료형 연산 
#리스트 자료형 ( = array 배열)

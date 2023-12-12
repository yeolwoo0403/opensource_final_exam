# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

numbers=[8, 30, 17, 2, 23]  # numbers를 [8,30,17,2,23]으로 리스트를 정의하였다.

def solution(numbers): 	#def를 이용하여 numbers를 매개변수로 하는 solution함수를 정의한다.
    numbers = list(map(str, numbers))	#numbers 안에 각 숫자들을 문자열로 바꿔 새로운 리스트를 만들도록 하였다.			
    for i in range(0, len(numbers)):	#for문을 이용해 0부터 numbers의 길이까지 반복하도록하였다.
        for j in range(i + 1, len(numbers)): #i+1위치에 있는 요소와 j번째 요소를 조합하여 큰수가 나오도록 순서를 정렬하기위해 for문을 이용했다.
            if numbers[i] + numbers[j] < numbers[j] + numbers[i]: #만약 j번째요소와 i+1번째 요소를 차례대로 이어붙인것이 i+1번째요소와 j번째요소를 이어붙인것 보다 작을경우
                numbers[i], numbers[j] = numbers[j], numbers[i]  #서로 순서를 바꾸도록 한다.
               
    answer = ''.join(numbers) #numbers를 answer에 문자열로 저장한다.
    return answer #answer을 리턴한다.

solution(numbers) #solution함수를 사용한다. 출력값 : '83023217' 


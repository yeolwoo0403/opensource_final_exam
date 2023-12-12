# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

age=23                                                    #age를 23으로 설정하였다.
def solution(age):					  #def를 사용하여 age를 매개변수로 하는 함수 solution을 정의 한다.		
    PROGRAMMERS_857 = {					  #key(숫자)와 value(알파벳)을 쌍으로 가지는 PROGRAMMERS_857딕셔너리를 생성하였다.
        '0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e',
        '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'
    }
    answer = ''						#answer에 PROGRAMMERS_857식 나이를 저장할 빈 문자열을 생성하였다.							
    age_list = list(str(age))  				#숫자를 문자열로 바꾸어 문자열의 각 문자를 리스트에 저장하도록 하였다.  
    for i in range(0,len(age_list)):			# i가 0부터 age_list의 길이만큼 반복하도록 for문을 사용하였다.
       age_list[i] = PROGRAMMERS_857.get(age_list[i])	#딕셔너리 PROGRAMMERS_857에서 get함수를 사용하여 age_list[i]를 key로 value값을 age_list에 순차적으로 저장한다.
    answer = ''.join(age_list)				#answer에 리스트인 age_list를 이어붙여 하나의 문자열로 저장하도록 하였다.
    return answer					#answer을 리턴하도록 했다.

solution(age)
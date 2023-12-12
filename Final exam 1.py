#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201910 이름 : 이우열

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

my_string="lee woo yeol"         #my_string을 "lee woo yeol"로 설정하였다.
target="woo"                     #target을 "woo"로 설정하였다.
def solution(my_string, target): #def를 사용해 매개변수 my_string(="lee woo yeol"), target(="woo")을 입력으로 하는 solution함수를 생성한다.
    if target in my_string:      #내장함수 in을 사용하여 target(="woo")이 my_string(="lee woo yeol")에 있는지 판단하는 if문을 만들었다. 있으면 if문을 실행하도록 하였다.
        answer=1		 #target이 my_string에 있으면 answer=1이다.	
    elif target not in my_string:#target이 my_string에 있지 않으면 answer=0이다. 
        answer=0		
    return answer		#answer을 리턴하도록 하였다.	

solution(my_string,target) #target="woo"인경우
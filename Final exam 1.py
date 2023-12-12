my_string="lee woo yeol"         #my_string을 "lee woo yeol"로 설정하였다.
target="woo"                     #target을 "woo"로 설정하였다.
def solution(my_string, target): #def를 사용해 매개변수 my_string(="lee woo yeol"), target(="woo")을 입력으로 하는 solution함수를 생성한다.
    if target in my_string:      #내장함수 in을 사용하여 target(="woo")이 my_string(="lee woo yeol")에 있는지 판단하는 if문을 만들었다. 있으면 if문을 실행하도록 하였다.
        answer=1		 #target이 my_string에 있으면 answer=1이다.	
    elif target not in my_string:#target이 my_string에 있지 않으면 answer=0이다. 
        answer=0		
    return answer		#answer을 리턴하도록 하였다.	

solution(my_string,target) #target="woo"인경우
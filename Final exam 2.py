# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

letter="... .-.. .- -.-- . -.."                                                     #인상깊었던 단어인 slayed("무언가 엄청 잘 해냄"이라는 뜻)을 모스부호로 바꾸어서 letter에 문자열로 저장하였다.

def solution(letter):                                			   	    #def를 사용해 매개변수 letter를 입력으로 하는 solution함수를 정의하였다.			
     morse = {									   #key(모스부호)와 value(알파벳)을 쌍으로 가지는 morse딕셔너리를 생성하였다.
         '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z'
     }
     answer = ''	                                      #answer에 letter모스부호를 해석하여 넣을 빈 문자열을 생성하였다.							
     morse_letter = letter.split(" ")			      #letter을 split함수를 사용하여 공백을 기준으로 나눠 morse_letter에 리스트로 반환하도록 하였다.	
     for i in range(len(morse_letter)):			      #반복문 for문을 사용하여 i가 morse_letter의 길이만큼 반복하도록 하였다. len함수를 사용하여 morse_letter의 길이를 읽었다.
         morse_letter[i] = morse.get(morse_letter[i])         #get함수를 사용하여 key에 대응하는 value값을 morse_letter에 저장하도록하였다. 예) morse_letter[0]=morse.get('...')를 실행하면 morse_letter의 0번째 index는 s가 된다. 		      	      
     answer = ''.join(morse_letter)		              #answer에 리스트인 morse_letter를 이어붙여 하나의 문자열로 저장하도록 하였다. 
     return answer					      #answer을 리턴하도록 하였다.	

solution(letter)     
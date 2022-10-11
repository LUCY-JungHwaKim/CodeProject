def solution(s):
    answer = ""
    answer_lst = []
    
    s_lst = s.split(" ") ## 문자열 띄어쓰기를 기준으로 분할
    #answer += '"'
    
    for word in s_lst: ## 잘려진 단어들 반복문 수행
        
        fir_word = word.capitalize() ## 문자열 앞자리만 대문자 만드는 함수
        ## 문자열 전체 대문자행 --> Upper Ex) str.upper()
        ## 문자열 전체 소문자행 --> Lower Ex) str.lower()
        
        answer += fir_word + " "
    
    answer = answer[:-1]
    
    return answer
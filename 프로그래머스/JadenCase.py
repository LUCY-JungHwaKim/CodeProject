def solution(s):
    answer = ""
    answer_lst = []
    
    s_lst = s.split(" ") ## ���ڿ� ���⸦ �������� ����
    #answer += '"'
    
    for word in s_lst: ## �߷��� �ܾ�� �ݺ��� ����
        
        fir_word = word.capitalize() ## ���ڿ� ���ڸ��� �빮�� ����� �Լ�
        ## ���ڿ� ��ü �빮���� --> Upper Ex) str.upper()
        ## ���ڿ� ��ü �ҹ����� --> Lower Ex) str.lower()
        
        answer += fir_word + " "
    
    answer = answer[:-1]
    
    return answer
import random
words = open("후보낱말.txt", "r").read().split()

def judge(word1, word2):
    """word1은 직전 낱말, word2는 새로운 낱말"""
#    if word2 not in words:    #후보낱말 파일의 완성도가 높으면 주석해제
#        return False
    if len(word2) == 1:    # 한 글자 단어라면 False 반환
        return False
    if word1[-1] == word2[0]:    # 글자가 이어졌다면 True 반환
        return True
    else:    # 그 외의 경우 모두 False 반환
        return False

def word_selection(previous_word):
    if not previous_word:    # 새로 시작하는 경우
        return random.choice(words)
    else:
        # 역슬래시\를 사용하면 긴 문장을 나눠 바로 아랫줄에 이어서 쓸 수 있다.
        available_words = \
            [i for i in words if i[0] == previous_word[-1] and len(i) > 1]
        if not available_words:  # 사용 가능한 단어가 없다면
            return ''
        else:
            return random.choice(available_words)

def word_chain():
    user_word=''
    print("컴퓨터: 나부터 할게.")
    while True:  # 끝말잇기 시작
        computer_word = word_selection(user_word)    # 찾아 고르기
        if not computer_word:
            print("컴퓨터: 내가 졌다. 다시 해.")
            user_word = ''
            continue
        else:
            print(computer_word)    # 말하기
            
        user_word=input("나: ")    # 듣기
        
        if not judge(computer_word, user_word):    # 판단하기
            print("컴퓨터: 와! 내가 이겼다!")
            break

while True:  # 대화 시작
    user = input("나: ")
    if user == "끝!":
        print("컴퓨터: 또 보자.")
        break
    elif "안녕" in user:
        print("컴퓨터: 만나서 반가워.")
    elif "끝말잇기" in user:
        word_chain()
    else:
        print("컴퓨터: 무슨 말인지 잘 모르겠어.")


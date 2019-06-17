def make_title(title):
    title = title.split()    # 띄어쓰기를 기준으로, 영화 제목의 단어를 분할
    new_title = ''
    for each_word in title:
        new_title += each_word[0].upper() + each_word[1:].lower() + ' '
    return new_title[:-1]      # new_title의 마지막에 붙은 공백을 떼어낸 문자열을 반환


a = input('입력 : ')
b = a.replace(' ', '')    # 띄어쓰기 삭제
c = b.replace(',', '')    # 반점 삭제
d = c.replace('.', '')    # 온점 삭제
e = d.replace("'", '')    # 작은따옴표 삭제
print(e)

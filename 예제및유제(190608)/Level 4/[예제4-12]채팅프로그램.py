while True:
    user = input("나: ")
    if user == "끝!":
        print("컴퓨터: 또 보자.")
        break
    elif "안녕" in user:
        print("컴퓨터: 만나서 반가워.")
    else:
        print("컴퓨터: 무슨 말인지 잘 모르겠어.")



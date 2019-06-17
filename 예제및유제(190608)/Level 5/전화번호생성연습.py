import time
시작 = time.time()
for i in range(100):
    for j in range(100):
        pass
        # print("010-%s-%s" % (str(i).zfill(4), str(j).zfill(4)))
        # print("010%s%s" % (str(i).zfill(4), str(j).zfill(4)))
종료 = time.time()
print(종료-시작)

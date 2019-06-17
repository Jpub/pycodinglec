import zipfile
압축파일 = zipfile.ZipFile("그림.zip")
성공 = False
for i in range(10000):
    for j in range(10000):
        A = "010-%s-%s" % (str(i).zfill(4), str(j).zfill(4))
        B = "010%s%s" % (str(i).zfill(4), str(j).zfill(4))
        try:
            압축파일.extractall(pwd=A.encode())
            성공 = True
            break
        except:
            pass
        if 성공:
            break

        try:
            압축파일.extractall(pwd=B.encode())
            성공 = True
            break
        except:
            pass
        if 성공:
            break

압축파일.close()

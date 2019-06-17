import zipfile
import winsound
압축파일 = zipfile.ZipFile("그림.zip")
for i in range(100000000):
    a = str(i).zfill(8)[:4]
    b = str(i).zfill(8)[4:]
    c = "010-%s-%s" % (a, b)
    d = "010%s%s" % (a, b)
    try:
        압축파일.extractall(pwd=c.encode())
        break
    except:
        pass
    try:
        압축파일.extractall(pwd=d.encode())
        break
    except:
        pass
압축파일.close()
winsound.Beep(1000, 20000)

"""
内存缓冲
file-like Object: StringIO 和 BytesIo-在内存中操作str和bytes
"""
from io import StringIO
f = StringIO()
f.write('hello stringIO')
f.write('i love')
f.write(' python')
print(f.getvalue())

f = StringIO('life is short\n i use python!')
while True:
    line = f.readline()
    if line == '':
        break
    print(line.strip())

from io import BytesIO
f = BytesIO()
f.write('你好'.encode('utf-8'))
print(f.getvalue())
# print(f.getvalue().decode())



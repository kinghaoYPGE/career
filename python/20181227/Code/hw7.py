"""
21根棍子游戏:
   1.  用户选1-4根棍子
   2.  程序选1-4根棍子
   3.  用户和程序一次选的总数是5
   4.  谁选到最后一根棍子，判定谁输
"""

sticks = 21
while True:
    print('sticks left: ', sticks)
    sticks_taken = int(input('please choose sticks(1-4):'))
    if sticks == 1:
        print('you loose, because you take last stick.')
        break
    if sticks_taken >= 5 or sticks_taken <= 0:
        print('only can take 1-4 sticks')
        continue
    print('Computer taken:' , (5 - sticks_taken))
    sticks -= 5



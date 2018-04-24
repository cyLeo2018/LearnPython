#汉诺塔

def hanoitowers(n, a, b, c):
    if n == 1:
        print(a,'->',c)
    else:
        hanoitowers(n-1, a, c, b)
        hanoitowers(1, a, b, c)
        hanoitowers(n-1, b, a, c)

while True:

    print('按Q或q退出程序')
    num1 = input('输入汉诺塔盘子数:')
    if num1 == 'Q' or num1 == 'q':
        break
    else:
        hanoitowers(int(num1), 'A', 'B', 'C')

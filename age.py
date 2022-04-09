driving = input('請問你有沒有開過車？')
if driving != '有' or '沒有':
    print('只能輸入（有/沒有）')
    raise SystemExit

age = input('請問你的年齡？')
age = int(age)

if driving == '有':
    if age >= 18:
        print('正常')
    else:
        print('嗶嗶！警察杯杯抓起來！')

elif driving == '沒有':
    if age >= 18:
        print('一定是天龍人')
    else:
        print('乖小孩')


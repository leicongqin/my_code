num = input('请输入一串数字')
result = 1
for i in range(len(num)-1):
    shiwei = int(num[i])
    gewei = int(num[i+1])
    nn = shiwei*10+gewei
    if shiwei:
        if nn <= 25:
            result += 1

print(result)

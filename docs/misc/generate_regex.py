# 输出所有可能的排列
string = '^-+=@_#&!|'
for i in range(len(string)):
    for j in range(len(string)):
        print(string[i] + string[j] + ', ', end='')
    print('\n')
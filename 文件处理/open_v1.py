# open(r'文件处理.md', 'r') #r可以让windows格式的\正常生效
# f.close()

with open(r'文件处理.md', 'r', encoding='utf-8') as f: #使用with语句格式打开文件，不使用后，文件管理自动关闭
    strline = f.readlines()
    print(type(strline))
    print(strline)
    for line in strline:
        print(line)

    # l = list(f)
    # for line in l:
    #     print(line)
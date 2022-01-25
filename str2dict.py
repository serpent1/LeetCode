str1 = "k:1|k1:2|k2:3|k3:4"

def str2dict(str:str1):
    dict1 = dict()
    for items in str1.split('|'):
        key1,value=items.split(':')
        dict1[key1]=value
    return dict1

print(str2dict(str1))

s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')

s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')


d= {'a':24,'g':52,'i':12,'k':33}

value=lambda x:x[1]
print(value)


# 打包
a = 1, 10, 100
print(type(a), a)    # <class 'tuple'> (1, 10, 100)
# 解包
i, j, k ,m= a
print(i, j, k)







str1 = "k:1|k1:2|k2:3|k3:4"

def str2dict(str:str1):
    dict1 = dict()
    for items in str1.split('|'):
        key1,value=items.split(':')
        dict1[key1]=value
    return dict1

print(str2dict(str1))
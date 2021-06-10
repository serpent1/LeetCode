#题目: 对给定的一个字符串，找出有重复的字符，并给出其位置
#如：abcaaAB12ab12 输出：a, 1; a, 4; a, 5; a, 10; b, 2; b, 11; 1, 8; 1, 12; 2, 9; 2, 13

class solution(object):
    def str_postion(self,str1):
        length=len(str1)
        dic1=dict()
        for i in range(0,length):
            list1=list()
            for j in range(0,length):
                if str1[i]==str1[j]:
                    list1.append(j+1)
            key=str1[i]
            dic1[key]=list1
        for key1,value1 in list(dic1.items()):
            if len(value1)<=1:
                dic1.pop(key1)
        return dic1

if __name__=='__main__':
    str1='abcdabc'
    target=solution().str_postion(str1=str1)
    print(target)
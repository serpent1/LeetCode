class solution(object):
    def map_methods(self,str_set):
        maps={2:'abc',
              3:'def',
              4:'ghi',
              5:'jkl',
              6:'mno',
              7:'pqr',
              8:'stu',
              9:'wxyz'
              }
        n1=int(str_set[0])
        n2=int(str_set[1])
        str1=maps.get(n1)
        str2=maps.get(n2)
        methods_list=[]
        for letter1 in str1:
            for letter2 in str2:
                method=str(letter1+letter2)
                methods_list.append(method)
        return methods_list

if __name__=='__main__':
    target=solution()
    methods=target.map_methods('23')
    print(methods)
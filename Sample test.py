class solution(object):
    def list_sort(self,list1):
        length=len(list1)
        for i in range(0,length):
            for j in range(i,length):
                if list1[i]>list1[j]:
                    pass
                    #list1[i],list1[j]=list1[j],list1[i]
                else:
                    list1[i],list1[j]=list1[i],list1[j]
        return list1



if __name__=="__main__":
    #test_list=[9,8,7,6,5]
    test_list=[5,6,7,8,9]
    target=solution().list_sort(test_list)
    print(target)
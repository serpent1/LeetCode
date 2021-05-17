class solution(object):
    def two_sum(selft,numbers_list,target):
        left=0
        right=len(numbers_list)-1
        while True:
            if numbers_list[left]+numbers_list[right]==target:
                return [left+1,right+1]
                break
            elif numbers_list[left]+numbers_list[right]>target:
                right-=1
            else:
                left+=1



if __name__=="__main__":
    list1=input('Please input the target list!')
    list2=list(list1)
    list3=[]
    for i in list2:
        list3.append(int(i))
    target_number=input('please input the target number')
    number=int(target_number)
    target_result=solution().two_sum(numbers_list=list3,target=number)
    print(target_result)
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
    target=solution().two_sum([1,2,3,4,6],target=8)
    print(target)
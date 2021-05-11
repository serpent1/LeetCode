class solution(object):
    def methods_num(self,x):
        sum=0
        if x<=2:
            return x
        else:
            num=self.methods_num(x-1)+self.methods_num(x-2)
            return num


if __name__=="__main__":
    target=solution()
    number=target.methods_num(5)
    print(number)
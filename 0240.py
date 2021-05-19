class solution(object):
    def matrix(self,m,n):
        matrix_sample = []
        for i in range(m):
            for j in range(n):
                matrix_sample.append([i,i+j+1,i+j+2,i+j+3])
                break
        return matrix_sample



if __name__=="__main__":
    target=solution().matrix(5,5)
    for i in target:
        print(i)

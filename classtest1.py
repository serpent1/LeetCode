class Stranger(object):
    def __init__(self, gender=None, age=None, job=None):
        self.gender = gender
        self.age = age
        self.jobb = job


if __name__ == "__main__":
    # 创建一个“妹子”
    meizi = Stranger()

    # 设置妹子的属性
    meizi.gender = "female"
    meizi.age = 18
    meizi.job = "teacher"

    # 访问妹子的属性
    print("妹子信息:")
    print("性别:{gender}".format(gender=meizi.gender))
    print("年龄:{age}".format(age=meizi.age))
    print("职业:{job}".format(job=meizi.job))

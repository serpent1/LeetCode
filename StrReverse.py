# txt = "Hello World"[::-1]
# print(txt)
#
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:4])


# b = "Hello, World!"
# a=b[-5:-2]
# print(a)
# print(a[::-1])

import json

x = {
  "name": "Bill",
  "age": 63,
  "married": True,
  "divorced": False,
  "children": ("Jennifer","Rory","Phoebe"),
  "pets": None,
  "cars": [
    {"model": "Porsche", "mpg": 38.2},
    {"model": "BMW M5", "mpg": 26.9}
  ]
}

# print(json.dumps(x,indent=3))

# import re
#
# txt = "China is a great country"
# x = re.search("^China.*country$", txt)
# if (x):
#   print("YES! We have a match!")
# else:
#   print("No match")

# thisset = {"apple", "banana", "cherry"}
#
# print("banana" in thisset,len(thisset))
#
# thisset.add("apple")
# thisset.update(["apple","shanghai"])
#
# for i in thisset:print(i)


# thisset = {"apple", "banana", "cherry"}
#
# del thisset
#
# print(thisset)
# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# result=tri_recursion(6)
#
# print(result)


import random
import threading


class A:
    setA = set()
    setB = set()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    threads = []

    def fun(self, condition):
        with condition:
            for i in self.arr:
                r = random.randrange(1, 100)
                if r % 2 == 0 and i not in self.setB:
                    self.setA.add(i)
                elif i not in self.setA:
                    self.setB.add(i)

    def tFun(self):
        condition = threading.Condition()
        for i in range(10):
            print('this is {0} theard'.format(i+1))
            t = threading.Thread(target=self.fun, args=(condition,))
            self.threads.append(t)
            t.start()
        for t in self.threads:
            t.join()
        print(self.setA)
        print(self.setB)


a = A()
a.tFun()




mylist = ["a", "b", "a", "c", "c"]


def my_function(x):
    return list(dict.fromkeys(x))

mylist=my_function(mylist)
print(mylist)
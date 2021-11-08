import itchat

# nums = []
# for i in range(10):
#     nums.insert(0, i)
#
# print(nums)

itchat.auto_login()
friends_list = itchat.get_friends(update=True)
print(len(friends_list))
luohao = friends_list[0]
props = ['NickName', 'Signature', 'Sex']
for prop in props:
    print(luohao[prop])
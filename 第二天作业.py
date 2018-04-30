


# 计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？

# count=0
# sum=0
# while count<99:
#     count+=1
#     if count==88:
#         continue
#     elif count%2==0:
#         sum-= count
#     else:
#         sum+=count
# print(sum)


# ⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）
# a=0
# while a<3:
#     useradd=input('请输入用户名：')
#     password=input('请输入密码  ：')
#     a=a+1
#     if  useradd=='小灰狗' and password=='123':
#         print('登陆成功')
#         break
#     else:
#         msg='用户名或者密码错误,您还有%s次登陆计划' % (3-a)
#         print(msg)


# 制作趣味模板程序需求：等待⽤户输⼊名字、地点、爱好，根据⽤户的名字和爱好进⾏任意现实 如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
# name=input('请输入您的名字：')
# place=input('请输入你喜欢去得地方：')
# intrest=input('请输入你最喜欢在这个地方干什么：')
# msg='敬爱可亲的%s，最喜欢在%s地方%s' % (name,place,intrest)
# print(msg)


#   等待⽤户输⼊内容，检测⽤户输⼊内容中是否包含敏感字符？如果存在敏感字符提示“存在敏感字符请重新输⼊”，
# 并允许⽤户重新输⼊并打印。敏感字符：“⼩粉嫩”、“⼤铁锤”
# m=True
# while m:
#     intrest = input('请输入你的爱好：')
#     if intrest=='小粉嫩'or intrest=='大铁锤':
#         print('存在敏感字符请重新输⼊')
#     else:
#         m=False
#         print('输入成功')

# classmates=['a','b','d','g','小奶牛']
# # print(classmates)
# # print(len(classmates))
# # print(classmates[-])
# classmates.append('小鸡鸡')
# print(classmates)
# classmates.insert(3,'ppp')
# print(classmates)
# classmates.pop()
# print(classmates)
# classmates.pop(5)
# print(classmates)
# classmates[2]='跳蛋'
# print(classmates)

# t=(1,2,'p','跳蛋')
# print(t)
#
# print(t)
# print(t[0])







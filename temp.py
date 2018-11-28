import random
import re

list1 = [1,2,3]
print(random.choice(list1))
myList = ['青海省','内蒙古自治区','西藏自治区','新疆维吾尔自治区','广西壮族自治区']
myList.sort(key = lambda i:len(i),reverse=True)
print(myList)
print(myList[0], myList[-1])


def isAllZh(s):
    for c in s:
        if not ('\u4e00' <= c <= '\u9fa5'):
            return False
    return True


#判断一段文本中是否包含简体中文
# zhmodel = re.compile(u'[\u4e00-\u9fa5]')    #检查中文
zhmodel = re.compile(u'[^\u4e00-\u9fa5]')   #检查非中文
contents = u'进来撒娇ddd地方ss'
match = zhmodel.search(contents)
print(match)
if match:
    print(contents)
else:
    print(u'没有包含中文')


i = None
if i == None:
    print(None)
else:
    print(123)

print('#################')

list1 = ['赞赞赞', '大大大', '搞搞搞']
list2 = "按时打卡发链接"

print(list2[-1],list2[0])
# startWordsList = chengYuPandas[chengYuPandas.str.startswith(lastWord, na=False)].values.tolist()

# 根据val排序dict


d={'a':1,'c':3,'b':2}    # 首先建一个字典d
 
#d.items()返回的是： dict_items([('a', 1), ('c', 3), ('b', 2)])
for i in range(n):
    dict1[i] = dict1.setdefault(dict1[i],0) + 1
d_order=sorted(dict1.items(),key=lambda x:x[1],reverse=False) 
#出来就不是dict格式了 

                                                       
print(list(d.values())[0] == list(d.values())[1])   

list(d.values())将值对应成list
d.values()[0]第一个value的值
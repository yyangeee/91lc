d={'a':1,'c':3,'b':2} 
dict1 = {}   # 首先建一个字典d
nums = [1,2,2,4,4,6,7,8,9]
#d.items()返回的是： dict_items([('a', 1), ('c', 3), ('b', 2)])
for i in range(len(nums)):
    dict1[nums[i]] = dict1.setdefault(nums[i],0) + 1
#d_order=sorted(dict1.items(),key=lambda x:x[1],reverse=False)  
#print(d_order)
print(d)                                                   
print(list(dict1.values()))   
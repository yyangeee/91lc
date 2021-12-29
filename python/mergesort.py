
if __name__ == "__main__":
    return merge_sort(lst)

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) / 2
    left = merge_sort(lst[:middle])     # 通过不断递归，将原始序列拆分成n个小序列
    right = merge_sort(lst[middle:])
    return merge(left, right)
#自定义，分治思想考虑合并的两个子部分
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):  # 比较传入的两个子序列，对两个子序列进行排序
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])         # 将排好序的子序列合并
    result.extend(right[j:])
    return result


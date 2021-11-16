class Node:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_
def list2link(List):
    head = Node(List[0])#创建一个头节点并将list第一个值赋值给头结点
    p = head#创建头指针
    for i in range(1, len(List)):#list从第二位开始遍历
        p.next = Node(List[i])#下一个结点p.next指向list值
        p = p.next#指针往下移动
    return head#返回头结点

if __name__ == "__main__":
    old_list = [1, 2, 3, 4, 5]
    link = list2link(old_list)

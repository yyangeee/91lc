

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
def list2link(List):
    head = Node(List[0])
    p = head
    for i in range(1, len(List)):
        p.next = Node(List[i])
        p = p.next
    return head
def merge(l1,l2):
    cur = head = Node()
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1               
            l1 = l1.next
        else:
            cur.next = l                
            l2 = l2.next
        cur = cur.next 
    cur.next = l1 if l1 else l2
    return head.next



if __name__ == "__main__":
    l1 = [1,2,4]
    link1 = list2link(l1)
    l2 = [1,3,4]
    link2 = list2link(l2)
    q = merge(link1,link2)
    print(q)




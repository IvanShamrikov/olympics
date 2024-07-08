# Картинка https://leetcode.com/problems/merge-two-sorted-lists/description/
# https://prnt.sc/yJIBeN3rGckn

# Перед цим завданням треба зробити підготовчу роботу по рекурсіям і звязним
# спискам, бо неподготовлені діти тупо не зможуть зрозуміти рекурсію як вона є



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a3 = ListNode(4)
a2 = ListNode(2, a3)
a1 = ListNode(1, a2)

b3 = ListNode(4)
b2 = ListNode(3, b3)
b1 = ListNode(1, b2)


def foo(linked_list1, linked_list2):
    if linked_list1.val == None:
        return linked_list2
    if linked_list2.val == None:
        return linked_list1

    if linked_list1.val < linked_list2.val:
        linked_list1.next = foo(linked_list1.next, linked_list2)
        return linked_list1
    else:
        linked_list2.next = foo(linked_list2.next, linked_list1)
        return linked_list2

foo(a1, b1)

while a1 != None:
    print(a1.val)
    a1 = a1.next
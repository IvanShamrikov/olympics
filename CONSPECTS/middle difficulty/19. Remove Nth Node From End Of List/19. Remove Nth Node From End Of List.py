 # Given the head of a linked list, remove the nth node from the end of the list and return its head.
 #
 # Input: head = [1,2,3,4,5], n = 2
 # Output: [1,2,3,5]
 # Example 2:
 #
 # Input: head = [1], n = 1
 # Output: []
 # Example 3:
 #
 # Input: head = [1,2], n = 1
 # Output: [1]

# Можна йти тільки з першого і далі.
# Перед тим, як давати цю задачу, треба дати лекцію на звязні списки, і шо це не масив.



 # Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, val=0, next=None):
 #         self.val = val
 #         self.next = next

 class Solution:
     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         counter = 0 #к-сть елементів в послідовності
         head_tmp = head #temporary head - тимчасова змінна для виконання операцій

         while head != None: #Поки ми не пройдемо всю цепочку і в об'єкті head не опиниться None
             head = head.next  #поточний об'єкт переписуємо наступним.
             counter += 1 #лічильник об'єктів +1
         head = head_tmp #повертаємо об'єкт head в початковий стан

         while counter - n - 1 > 0: #поки ми не дійшли до останнього об'єкта перед заданою диркою
             counter -= 1
             head = head.next #переход до наступного об'єкту

         #перезаписуємо поле next, перескакуючи через об'єкт
         head.next = head.next.next

         return head
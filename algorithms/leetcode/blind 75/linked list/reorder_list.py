'''
https://leetcode.com/problems/reorder-list/
'''


def reorderList(head):

    # hare tortoise
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    prev = slow.next = None

    # reverse linked list
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    # merge two lists
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

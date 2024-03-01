class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev

def merge_sort_list(head):
    if not head or not head.next:
        return head

    # Розділення списку на дві частини
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    # Рекурсивне сортування двох половин
    left = merge_sort_list(head)
    right = merge_sort_list(next_to_middle)

    # Злиття відсортованих половин
    sorted_list = sorted_merge(left, right)
    return sorted_list

def get_middle(head):
    if not head:
        return head

    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def sorted_merge(a, b):
    result = None
    if not a:
        return b
    if not b:
        return a

    if a.value <= b.value:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)
    return result


def merge_sort_list(head):
    if not head or not head.next:
        return head

    # Розділення списку на дві частини
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    # Рекурсивне сортування двох половин
    left = merge_sort_list(head)
    right = merge_sort_list(next_to_middle)

    # Злиття відсортованих половин
    sorted_list = sorted_merge(left, right)
    return sorted_list

def get_middle(head):
    if not head:
        return head

    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def sorted_merge(a, b):
    result = None
    if not a:
        return b
    if not b:
        return a

    if a.value <= b.value:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)
    return result


def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next

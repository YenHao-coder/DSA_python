from collections import deque

"""Stack 實作 (list)"""
stack = []
stack.append("Page_A")
stack.append("Page_B")
top_item = stack.pop()
print(f"Stack Pop:{top_item}")

"""Queue 實作 (deque)"""
queue = deque()
queue.append("Customer_1")
queue.append("Customer_2")
first_item = queue.popleft()
print(f"Queue Dequeue: {first_item}")
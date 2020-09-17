"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# 1. Using array as underlying structure
# Remove from head, add to tail


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage):
#             popped_element = self.storage.pop(0)
#             return popped_element
#         else:
#             return None

from singly_linked_list import LinkedList
# 2. Using linked list as underlying structure


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        count = 0
        if self.storage.head is None:
            return count
        else:
            cur_node = self.storage.head
            while cur_node is not None:
                cur_node = cur_node.get_next_node()
                count += 1
            return count

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage):
            popped_element = self.storage.pop(0)
            return popped_element
        else:
            return None
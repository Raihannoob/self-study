class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value


class DoublelinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail= node
            self.size += 1

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{','.join(str(val) for val in vals)}]"
    def remove_node(self,node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        self.size -= 1
    def remove(self,value):
        node = self.head
        while  node is not None:
            if node.val == value :
                self.remove_node(node)
                break
            node = node.next
    def remove_last(self):
        if self.tail is not None:
            self.remove_node(self.tail)

    def back(self):
        return self.tail.val
    def head(self):
        return  self.head.val

#my_list = DoublelinkList()
#my_list.add(1)
#my_list.add(5)
#my_list.add(6)
#my_list.add(8)
#my_list.add(7)
#my_list.add(7)
#print(my_list)
#my_list.remove(8)
#my_list.remove(7)
#my_list.remove_last()
#print(my_list)
#print(my_list.size)
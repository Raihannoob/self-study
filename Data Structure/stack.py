from doublelinklist import DoublelinkList
class stack:
    def __init__(self):
        self.__list = DoublelinkList()


    def push(self,val):
        self.__list.add(val)

    def pop(self):
        val = self.__list.back()
        self.__list.remove_last()
        return  val

    def is_empty(self):
        return self.__list.size == 0

    def peek(self):
        return self.__list.back()
    def __len__(self):
        return  self.__list.size

#my_stack = stack()
#my_stack.push(1)
#my_stack.push(2)
#my_stack.push(3)
#print(my_stack.peek())
#my_stack.push(66)
#print(my_stack.peek())
#my_stack.push(5)
#my_stack.pop()
#print(my_stack.peek())
#print(len(my_stack))
#print(my_stack.pop())
#print(len(my_stack))

class Queue:
    def __init__(self):
        self.__list = DoublelinkList()

    def enqueue(self,val):
        self.__list.add(val)

    def dequeue(self):
            val = self.__list.front()
            self.__list.remove_front()
            return val
    def front(self):
        return self.__list.front()

    def is_empty(self):
        return self.__list.size == 0

    def __len__(self):
        return self.__list.size

    def printqueue(self):
        print("queue elements are:")
        temp = self.__list.head
        while temp is not None:
            print(temp.val, end="->")
            temp = temp.next



#my_queue = Queue()
#my_queue.enqueue(1)
#my_queue.enqueue(12)
#my_queue.enqueue(13)
#my_queue.enqueue(14)
#my_queue.enqueue(15)
#my_queue.enqueue(16)
#print(len(my_queue))
#print(my_queue.dequeue())
#print(len(my_queue))
#print(my_queue.front())
#rint(my_queue.dequeue())
#print(my_queue.front())
#y_queue.printqueue()

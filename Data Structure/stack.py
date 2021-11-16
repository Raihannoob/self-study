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

my_stack = stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.peek())
my_stack.push(66)
print(my_stack.peek())
my_stack.push(5)
my_stack.pop()
print(my_stack.peek())
print(len(my_stack))
print(my_stack.pop())
print(len(my_stack))



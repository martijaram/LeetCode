class Node:
    value = None
    next = None
    
    
    def __init__(self, value):
        self.value = value
        self.next = next


class MyQueue:
    rightlink = None
    leftlink = None
    
    def __init__(self):
        self.rightlink = []
        self.leftlink = []

    def push(self, x: int) -> None:
        while (self.rightlink != []):
            element = self.rightlink.pop()
            self.leftlink.append(element)
            
        self.leftlink.append(x)
        
        print(self.leftlink)
            
        while (self.leftlink != []):
            print("it works: " + str(x))
            
            element = self.leftlink.pop()
            self.rightlink.append(element)
        
        print(self.rightlink)

    def pop(self) -> int:
        if (self.leftlink is not []):
            return self.rightlink.pop()

        

    def peek(self) -> int:
        if (self.rightlink is not []):
            return self.rightlink[-1]


    def empty(self) -> bool:
        return self.rightlink == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
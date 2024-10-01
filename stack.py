class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        self.stack = []
        pass
    def push(self,val) -> None:
        self.stack.append(val)
        pass
    def empty(self) -> bool:
        if len(self.stack)==0:
            return True
        else:
            return False
        pass
    def pop(self) -> None:
        if not self.empty():
            return self.stack.pop()
        return None
        pass
    def top(self):
        if self.empty()==False:
            return self.stack[-1]

    # You can implement this class however you like

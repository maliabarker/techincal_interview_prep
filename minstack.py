'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

'''
'''
Inputs: 
    minstack: none
    push: int
    pop: none
    top: none
    getMin: none
Outputs:
    minstack: none
    push: none
    pop: none
    top: int
    getMin: int
EXAMPLE:
input: "MinStack","push(-2)","push(0)","push(-3)","getMin","pop","top","getMin"
output: [null,null,null,null,-3,null,0,-2]
<example code>
    MinStack 
    minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2
'''


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        print('PUSH')
        
        # Check if the stack is empty or not
        if not self.stack:
            # if empty
            print('PUSH-Nothing there')
            # append tuple with value and minimum (which equals value)
            self.stack.append((val, val))
            print(self.stack)
        else:
            # if not empty
            print('PUSH-Something here')
            print(self.stack[-1][1])
            
            # append tuple with value and minimum value to store for future use
            self.stack.append((val, min(val, self.stack[-1][1])))
    
    def pop(self) -> None:
        print('POP')
        print(self.stack)
        # check if there is something in stack, if there is perform pop
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        print('TOP')
        # check if theres something in stack
        if self.stack:
            print(self.stack[-1][0])
            return self.stack[-1][0]
        else:
            return None

    def getMin(self) -> int:
        print('MIN')
        if self.stack:
            print(self.stack[-1][1])
            return self.stack[-1][1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
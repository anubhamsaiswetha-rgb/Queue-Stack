class stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
    
    def push(self, value):
        if self.isFull():
            print("Stack Overflow!")
        else:
            self.stack.append(value)
            print(value, "pushed")

    def pop(self):
        if self.isEmpty():
            print("stack underflow!")
        else:
            print(self.stack.pop(), "popped")
    
    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print("Top: ", self.stack[-1])

    def isEmpty(self):
        return len(self.stack) == 0
    
    def isFull(self):
        return len(self.stack) == self.size
    
    def display(self):
        print(self.stack)

s = stack(5)
while True:
    while True:
        print("\n--- stack menu ---")
        print("1. push")
        print("2. pop")
        print("3. peek")
        print("4. isEmpty")
        print("5. isFull")
        print("6. display")
        print("7. exit")
        choice = int(input("Enter the choice:"))

        if choice == 1:
            val = int(input("enter choice: "))
            s.push(val)

        elif choice == 2:
            s.pop()
        
        elif choice == 3:
            s.peek()

        elif choice ==4:
            print(s.isEmpty())
        
        elif choice == 5:
            print(s.isFull())
        
        elif choice == 6:
            s.display()
            
        elif choice == 7:
            break
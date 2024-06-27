

class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of the queue.
        
        Args:
        x (int): Element to be pushed onto the queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of the queue and returns that element.
        
        Returns:
        int: The element removed from the front of the queue.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        
        Returns:
        int: The element at the front of the queue.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        
        Returns:
        bool: True if the queue is empty, False otherwise.
        """
        return not self.stack1 and not self.stack2

# Example usage
if __name__ == "__main__":
    queue = MyQueue()

    # Push elements onto the queue
    queue.push(1)
    queue.push(2)
    queue.push(3)

    # Print the queue state
    print(f"Queue elements after pushes: {queue.stack1}")

    # Pop an element from the queue
    popped_element = queue.pop()
    print(f"Popped element: {popped_element}")

    # Peek at the front element of the queue
    front_element = queue.peek()
    print(f"Front element (peek): {front_element}")

    # Check if the queue is empty
    is_empty = queue.empty()
    print(f"Is the queue empty? {is_empty}")
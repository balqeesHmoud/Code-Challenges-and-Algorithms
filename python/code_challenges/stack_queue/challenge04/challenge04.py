# Write here the code challenge solution

from queue import Queue

def reverse_queue(queue):
    """
    Reverses the given queue.
    
    Args:
    queue (Queue): The queue to be reversed.
    
    Returns:
    Queue: The reversed queue.
    """
    stack = []
    while not queue.empty():
        stack.append(queue.get())
    
    while stack:
        queue.put(stack.pop())
    
    return queue

def main():
    q = Queue()
    for i in [5, 4, 3, 2, 1]:
        q.put(i)
    
    print("Original Queue: ", end="")
    temp_q = Queue()
    while not q.empty():
        item = q.get()
        print(f"[{item}]", end="->" if not q.empty() else "")
        temp_q.put(item)
    print()
    
    q = temp_q  # Restore the original queue for reversal
    reversed_q = reverse_queue(q)
    
    print("Reversed Queue: ", end="")
    while not reversed_q.empty():
        item = reversed_q.get()
        print(f"[{item}]", end="->" if not reversed_q.empty() else "")
    print()

if __name__ == "__main__":
    main()

# Write here the code challenge solution
def delete_middle(stack):
    """
    Delete the middle element from a stack.

    Args:
    stack (list): The stack from which the middle element should be deleted.

    Returns:
    list: The stack after the middle element has been deleted.
    """
    if not stack:
        return stack
    
    mid_index = len(stack) // 2
    if len(stack) % 2 == 0:
        mid_index -= 1
    
    new_stack = stack[:mid_index] + stack[mid_index + 1:]
    return new_stack

if __name__ == "__main__":
    test_stack1 = [1, 2, 3, 4, 5]
    test_stack2 = [1, 2, 3, 4]
    print("Original stack:", test_stack1)
    print("Updated stack:", delete_middle(test_stack1))
    print("Original stack:", test_stack2)
    print("Updated stack:", delete_middle(test_stack2))

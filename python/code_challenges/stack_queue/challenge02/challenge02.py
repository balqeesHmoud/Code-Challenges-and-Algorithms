
def is_valid(s: str) -> bool:
    """
    Determine if the input string containing just the characters '(', ')', '{', '}', '[' and ']', is valid.

    An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.

    Parameters:
    s (str): Input string containing just the characters '(', ')', '{', '}', '[' and ']'.

    Returns:
    bool: True if the input string is valid, False otherwise.
    """
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        elif char in bracket_map.values():
            stack.append(char)
    return not stack

def main():
    test_cases = ["()", "()[]{}", "[({}]", "[(hello)()]", "[{(())}]", "", "(([]){})", "([)]", "{[]}"]
    for case in test_cases:
        result = is_valid(case)
        print(f"is_valid('{case}') = {result}")

if __name__ == "__main__":
    main()

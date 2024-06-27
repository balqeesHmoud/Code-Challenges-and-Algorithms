from challenge02 import ListNode, Solution
import unittest

class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class methods.
    """
    def list_to_linkedlist(self, elements):
        """
        Converts a list of elements into a linked list.

        Args:
            elements (list): List of elements.

        Returns:
            ListNode: Head of the linked list.
        """
        head = ListNode(elements[0])
        current = head
        for element in elements[1:]:
            current.next = ListNode(element)
            current = current.next
        return head

    def linkedlist_to_list(self, node):
        """
        Converts a linked list into a list.

        Args:
            node (ListNode): Head of the linked list.

        Returns:
            list: List of node values.
        """
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def test_middleNode(self):
        """
        Tests the middleNode method of the Solution class.
        """
        sol = Solution()
        
        head1 = self.list_to_linkedlist([1, 2, 3, 4, 5])
        result1 = sol.middleNode(head1)
        self.assertEqual(self.linkedlist_to_list(result1), [3, 4, 5])
        
        head2 = self.list_to_linkedlist([1, 2, 3, 4, 5, 6])
        result2 = sol.middleNode(head2)
        self.assertEqual(self.linkedlist_to_list(result2), [4, 5, 6])

if __name__ == '__main__':
    # Running tests and printing results
    unittest.main()
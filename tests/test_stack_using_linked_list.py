"""Test cases for stack_using_linked_list.py.
"""
import unittest
from abstract_data_type.stack_using_linked_list import StackUsingLinkedList

class TestStackUsingLinkedList(unittest.TestCase):
    """Tests the functionality of StackUsingLinkedList.
    """

    def test_init(self):
        """Tests __init__().
        """
        stack = StackUsingLinkedList()
        self.assertTrue(stack.is_empty())
        with self.assertRaises(AttributeError):
            stack.top()
        self.assertEqual(str(stack), '')

    def test_iter(self):
        """Tests __iter__().
        """
        stack = StackUsingLinkedList()
        iter_stack = iter(stack)
        with self.assertRaises(StopIteration):
            next(iter_stack)

        stack.push(1)
        iter_stack = iter(stack)
        val = next(iter_stack)
        self.assertEqual(val, '1')
        with self.assertRaises(StopIteration):
            next(iter_stack)

        stack.push(2)
        iter_stack = iter(stack)
        val = next(iter_stack)
        self.assertEqual(val, '2')
        val = next(iter_stack)
        self.assertEqual(val, '1')
        with self.assertRaises(StopIteration):
            next(iter_stack)

    def test_str(self):
        """Tests __str__().
        """
        stack = StackUsingLinkedList()
        self.assertEqual(str(stack), '')

        stack.push(1)
        self.assertEqual(str(stack), '1')

        stack.push(2)
        self.assertEqual(str(stack), '2 1')

    def test_len(self):
        """Tests __len__().
        """
        stack = StackUsingLinkedList()
        self.assertEqual(len(stack), 0)

        stack.push(1)
        self.assertEqual(len(stack), 1)

        stack.push(2)
        self.assertEqual(len(stack), 2)

        stack.pop()
        self.assertEqual(len(stack), 1)

        stack.pop()
        self.assertEqual(len(stack), 0)

    def test_push(self):
        """Tests push().
        """
        stack = StackUsingLinkedList()

        stack.push(1)
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.top(), 1)
        self.assertEqual(str(stack), '1')

        stack.push(3)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.top(), 3)
        self.assertEqual(str(stack), '3 1')

        stack.push(2)
        self.assertEqual(len(stack), 3)
        self.assertEqual(stack.top(), 2)
        self.assertEqual(str(stack), '2 3 1')

    def test_remove(self):
        """Tests remove().
        """
        stack = StackUsingLinkedList()
        stack.push(1)
        stack.push(3)
        stack.push(2)

        val = stack.pop()
        self.assertEqual(val, 2)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.top(), 3)
        self.assertEqual(str(stack), '3 1')

        val = stack.pop()
        self.assertEqual(val, 3)
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.top(), 1)
        self.assertEqual(str(stack), '1')

        val = stack.pop()
        self.assertEqual(val, 1)
        self.assertTrue(stack.is_empty())
        with self.assertRaises(AttributeError):
            stack.top()
        self.assertEqual(str(stack), '')

        with self.assertRaises(IndexError):
            stack.pop()

    def test_is_empty(self):
        """Tests is_empty().
        """
        stack = StackUsingLinkedList()
        self.assertTrue(stack.is_empty())
        self.assertEqual(len(stack), 0)

        stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertEqual(len(stack), 1)

        stack.push(2)
        self.assertFalse(stack.is_empty())
        self.assertEqual(len(stack), 2)

        stack.pop()
        self.assertFalse(stack.is_empty())
        self.assertEqual(len(stack), 1)

        stack.pop()
        self.assertTrue(stack.is_empty())
        self.assertEqual(len(stack), 0)


    def test_top(self):
        """Tests top().
        """
        stack = StackUsingLinkedList()

        with self.assertRaises(AttributeError):
            stack.top()

        stack.push(1)
        self.assertEqual(stack.top(), 1)

        stack.push(1)
        self.assertEqual(stack.top(), 1)

        stack.push(2)
        self.assertEqual(stack.top(), 2)

        stack.push(0)
        self.assertEqual(stack.top(), 0)

        stack.pop()
        self.assertEqual(stack.top(), 2)

        stack.pop()
        self.assertEqual(stack.top(), 1)

        stack.pop()
        self.assertEqual(stack.top(), 1)

        stack.pop()
        with self.assertRaises(AttributeError):
            stack.top()

if __name__ == '__main__':
    unittest.main()

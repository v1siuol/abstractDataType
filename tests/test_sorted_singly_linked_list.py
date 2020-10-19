"""Test cases for sorted_singly_linked_list.py.
"""
import unittest
from abstract_data_type.sorted_singly_linked_list import SortedSinglyLinkedList

class TestSortedSinglyLinkedList(unittest.TestCase):
    """Tests the functionality of SortedSinglyLinkedList.
    """

    def test_init(self):
        """Tests __init__().
        """
        linked_list = SortedSinglyLinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertIsNone(linked_list.top())
        self.assertIsNone(linked_list.bot())
        self.assertEqual(str(linked_list), '')

    def test_iter(self):
        """Tests __iter__().
        """
        linked_list = SortedSinglyLinkedList()
        iter_linked_list = iter(linked_list)
        with self.assertRaises(StopIteration):
            next(iter_linked_list)

        linked_list.insert(1)
        iter_linked_list = iter(linked_list)
        next(iter_linked_list)
        with self.assertRaises(StopIteration):
            next(iter_linked_list)

        linked_list.insert(2)
        iter_linked_list = iter(linked_list)
        next(iter_linked_list)
        next(iter_linked_list)
        with self.assertRaises(StopIteration):
            next(iter_linked_list)

    def test_str(self):
        """Tests __str__().
        """
        linked_list = SortedSinglyLinkedList()
        self.assertEqual(str(linked_list), '')

        linked_list.insert(1)
        self.assertEqual(str(linked_list), '1')

        linked_list.insert(2)
        self.assertEqual(str(linked_list), '1 2')

    def test_len(self):
        """Tests __len__().
        """
        linked_list = SortedSinglyLinkedList()
        self.assertEqual(len(linked_list), 0)

        linked_list.remove(1)
        self.assertEqual(len(linked_list), 0)

        linked_list.insert(1)
        self.assertEqual(len(linked_list), 1)

        linked_list.insert(2)
        self.assertEqual(len(linked_list), 2)

    def test_insert(self):
        """Tests insert().
        """
        linked_list = SortedSinglyLinkedList()

        linked_list.insert(1)
        self.assertEqual(len(linked_list), 1)
        self.assertEqual(linked_list.top(), 1)
        self.assertEqual(linked_list.bot(), 1)
        self.assertEqual(str(linked_list), '1')

        linked_list.insert(2)
        self.assertEqual(len(linked_list), 2)
        self.assertEqual(linked_list.top(), 1)
        self.assertEqual(linked_list.bot(), 2)
        self.assertEqual(str(linked_list), '1 2')

        linked_list.insert(3)
        self.assertEqual(len(linked_list), 3)
        self.assertEqual(linked_list.top(), 1)
        self.assertEqual(linked_list.bot(), 3)
        self.assertEqual(str(linked_list), '1 2 3')

        linked_list.insert(2)
        self.assertEqual(len(linked_list), 4)
        self.assertEqual(linked_list.top(), 1)
        self.assertEqual(linked_list.bot(), 3)
        self.assertEqual(str(linked_list), '1 2 2 3')

        linked_list.insert(-1)
        self.assertEqual(len(linked_list), 5)
        self.assertEqual(linked_list.top(), -1)
        self.assertEqual(linked_list.bot(), 3)
        self.assertEqual(str(linked_list), '-1 1 2 2 3')

        linked_list.insert(3)
        self.assertEqual(len(linked_list), 6)
        self.assertEqual(linked_list.top(), -1)
        self.assertEqual(linked_list.bot(), 3)
        self.assertEqual(str(linked_list), '-1 1 2 2 3 3')

    def test_remove(self):
        """Tests remove().
        """
        linked_list = SortedSinglyLinkedList()
        linked_list.insert(1)
        linked_list.insert(2)
        linked_list.insert(3)
        linked_list.insert(2)
        linked_list.insert(-1)
        linked_list.insert(3)

        linked_list.remove(3)
        self.assertEqual(len(linked_list), 5)
        self.assertEqual(linked_list.top(), -1)
        self.assertEqual(linked_list.bot(), 3)
        self.assertEqual(str(linked_list), '-1 1 2 2 3')

        linked_list.remove(-1)
        self.assertEqual(len(linked_list), 4)
        self.assertEqual(linked_list.top(), 1)
        self.assertEqual(linked_list.bot(), 3)
        self.assertEqual(str(linked_list), '1 2 2 3')

        linked_list.remove(2)
        self.assertEqual(len(linked_list), 3)
        self.assertEqual(linked_list.top(), 1)
        self.assertEqual(linked_list.bot(), 3)
        self.assertEqual(str(linked_list), '1 2 3')

        linked_list.remove(3)
        self.assertEqual(len(linked_list), 2)
        self.assertEqual(linked_list.top(), 1)
        self.assertEqual(linked_list.bot(), 2)
        self.assertEqual(str(linked_list), '1 2')

        # Tests non-exist value removal when linked list has multiple elements.
        linked_list.remove(3)
        self.assertEqual(len(linked_list), 2)
        self.assertEqual(linked_list.top(), 1)
        self.assertEqual(linked_list.bot(), 2)
        self.assertEqual(str(linked_list), '1 2')

        linked_list.remove(2)
        self.assertEqual(len(linked_list), 1)
        self.assertEqual(linked_list.top(), 1)
        self.assertEqual(linked_list.bot(), 1)
        self.assertEqual(str(linked_list), '1')

        # Tests non-exist value removal when linked list has only one element.
        linked_list.remove(2)
        self.assertEqual(len(linked_list), 1)
        self.assertEqual(linked_list.top(), 1)
        self.assertEqual(linked_list.bot(), 1)
        self.assertEqual(str(linked_list), '1')

        linked_list.remove(1)
        self.assertTrue(linked_list.is_empty())
        self.assertIsNone(linked_list.top())
        self.assertIsNone(linked_list.bot())
        self.assertEqual(str(linked_list), '')

        # Tests non-exist value removal when linked list is empty.
        linked_list.remove(1)
        self.assertTrue(linked_list.is_empty())
        self.assertIsNone(linked_list.top())
        self.assertIsNone(linked_list.bot())
        self.assertEqual(str(linked_list), '')

    def test_is_empty(self):
        """Tests is_empty().
        """
        linked_list = SortedSinglyLinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(len(linked_list), 0)

        linked_list.remove(1)
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(len(linked_list), 0)

        linked_list.insert(1)
        self.assertFalse(linked_list.is_empty())
        self.assertEqual(len(linked_list), 1)

        linked_list.insert(2)
        self.assertFalse(linked_list.is_empty())
        self.assertEqual(len(linked_list), 2)

    def test_top(self):
        """Tests top().
        """
        linked_list = SortedSinglyLinkedList()
        self.assertIsNone(linked_list.top())

        linked_list.insert(1)
        self.assertEqual(linked_list.top(), 1)

        linked_list.insert(1)
        self.assertEqual(linked_list.top(), 1)

        linked_list.insert(2)
        self.assertEqual(linked_list.top(), 1)

        linked_list.insert(0)
        self.assertEqual(linked_list.top(), 0)

    def test_bot(self):
        """Tests bot().
        """
        linked_list = SortedSinglyLinkedList()
        self.assertIsNone(linked_list.bot())

        linked_list.insert(1)
        self.assertEqual(linked_list.bot(), 1)

        linked_list.insert(1)
        self.assertEqual(linked_list.bot(), 1)

        linked_list.insert(2)
        self.assertEqual(linked_list.bot(), 2)

        linked_list.insert(0)
        self.assertEqual(linked_list.bot(), 2)

if __name__ == '__main__':
    unittest.main()

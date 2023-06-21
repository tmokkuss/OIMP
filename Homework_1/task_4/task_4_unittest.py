import unittest
import task_4


class MyTestCase(unittest.TestCase):
    def test_find_count_symbols(self):
        expected = [('c', 3), ('a', 2), ('b', 2)]
        data = 'aa bb ccc'
        self.assertListEqual(task_4.find_count_symbols(data), expected)

    def test_add_enters(self):
        expected = ['c', ', 3\n', 'a', ', 2\n', 'b', ', 2\n']
        data = [('c', 3), ('a', 2), ('b', 2)]
        self.assertEqual(task_4.add_enters(data), expected)


if __name__ == '__main__':
    unittest.main()
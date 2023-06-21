import unittest
import task_2


class MyTestCase(unittest.TestCase):
    def test_sort_data(self):
        expected = ["KP2.2-01.3 - Vedomost'\n", \
                   "KP2.2-10.3 - Vedomost'\n"]
        data = "KP2.2-10.3 - Vedomost'\n" \
               "KP2.2-01.3 - Vedomost'\n"
        self.assertEqual(task_2.sort_data(data), expected)


if __name__ == '__main__':
    unittest.main()
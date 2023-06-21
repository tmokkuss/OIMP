import unittest

import task_1


class Task1Test(unittest.TestCase):
    def test_get_grade_and_name(self):
        expected = "Котов Алексей,4\n"
        data = ['1. Котов Алексей: 4']
        self.assertEqual(task_1.get_grade_and_name(data)[0], expected)

    def test_alphabetical_sorting(self):
        expected = ["Бакушкин Даниил,3", "Белова Юлия,3"]
        data = ["Белова Юлия,3", "Бакушкин Даниил,3"]
        self.assertEqual(task_1.alphabetical_sorting(data), expected)


if __name__ == '__main__':
    unittest.main()

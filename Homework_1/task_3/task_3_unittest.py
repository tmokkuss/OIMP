import unittest
import task_3


class MyTestCase(unittest.TestCase):
    def test_1_format_text(self):
        expected = f'Lorem ipsum dolor\n' \
                    'sit amet,\n' \
                    'consectetur\n' \
                    'adipiscing elit, sed\n' \
                    'do eiusmod tempor\n' \
                    'incididunt ut labore\n' \
                    'et dolore magna\n' \
                    'aliqua.'
        data = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, ' \
               'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        self.assertEqual(task_3.format_text(data), expected)


if __name__ == '__main__':
    unittest.main()
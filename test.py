import unittest

from main import Door, Runner


class RunnerTest(unittest.TestCase):
    def setUp(self):
        self.runner = Runner({'door': Door()})

    def test_parse_gives_us_the_right_instance(self):
        command = self.runner.parse('unlock door')
        self.assertIsInstance(command.__self__, Door)


if __name__ == '__main__':
    unittest.main()

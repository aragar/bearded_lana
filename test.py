import unittest

from main import Door, Runner


class RunnerTest(unittest.TestCase):
    def setUp(self):
        self.runner = Runner({'door': Door()})

    def test_parse_gives_us_the_right_instance(self):
        command = self.runner.parse('unlock door')
        self.assertIsInstance(command.__self__, Door)


class DoorTests(unittest.TestCase):
    def setUp(self):
        self.door = Door()

    def test_the_door_can_be_unlocked(self):
        self.door.is_locked = True
        self.door.unlock()
        self.assertFalse(self.door.is_locked)

    def test_the_unlock_door_on_unlocked_door(self):
        self.door.is_locked = False
        self.door.unlock()
        self.assertFalse(self.door.is_locked)

if __name__ == '__main__':
    unittest.main()

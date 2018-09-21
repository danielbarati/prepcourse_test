import unittest
from exercise1 import hello_world

class TestExerciseSet(unittest.TestCase):

    def test_helloworld(self):
        self.assertEqual(hello_world(), 'Hello, world!')

if __name__ == '__main__':
    unittest.main()
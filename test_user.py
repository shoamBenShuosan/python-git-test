import unittest
from User import User

class TestUserConstructor(unittest.TestCase):
    def test_constructor(self):
        name = "John Doe"
        id = 1
        user = User(name, id)
        self.assertEqual(user.name, name)
        self.assertEqual(user.id, id)

        with self.assertRaises(TypeError):
            User(123, id)

if __name__ == '__main__':
    unittest.main()
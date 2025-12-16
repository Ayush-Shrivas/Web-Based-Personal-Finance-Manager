import unittest
from auth import register_user, login_user

class TestAuth(unittest.TestCase):
    def test_register_login(self):
        register_user("testuser", "pass")
        self.assertIsNotNone(login_user("testuser", "pass"))

if __name__ == "__main__":
    unittest.main()

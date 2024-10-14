import unittest

def login(username, password):
    if username == "usuario" and password == "contraseña":
        return True
    else:
        return False

class TestLogin(unittest.TestCase):
    def test_login_success(self):
        self.assertTrue(login("usuario", "contraseña"))

    def test_login_failure(self):
        self.assertFalse(login("usuario", "contraseña_incorrecta"))

if __name__ == '__main__':
    unittest.main()

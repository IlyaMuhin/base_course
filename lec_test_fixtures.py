import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Настройка начальных условий 
        # выполняется перед каждым тестом
        self.data = [1,2,3,4,5]

    def tearDown(self):
        # Очистка ресурсов, выполняется после каждого теста
        self.data = None

    def test_sum(self):
        total = sum(self.data)
        self.assertEqual(total, 15)

    def test_length(self):
        length = len(self.data)
        self.assertEqual(length, 5)

if __name__ == '__main__':
    unittest.main()

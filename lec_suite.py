import unittest

class MyTestCase(unittest.TestCase):
 def test_sum(self):
        result = 2 + 2
        self.assertEqual(result, 4)

class MyOtherTestCase(unittest.TestCase):
 def test_multiply(self):
        result = 3 * 5
        self.assertEqual(result, 15)

# Создание набора тестов
test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(MyTestCase))
test_suite.addTest(unittest.makeSuite(MyOtherTestCase))

# Создание и запуск тестового Исполнителя (test runner)
test_runner = unittest.TextTestRunner()
test_runner.run(test_suite)
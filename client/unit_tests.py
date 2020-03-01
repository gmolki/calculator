import unittest
import serverConnection as s


class TestSum(unittest.TestCase):

    def setUp(self):
        self.server = s.ServerConnection('http://127.0.0.1:5000/')

    # Different tests made to the addition operation
    # TEST 1:
    def test_addition1(self):

        operation = {'value1': '1',
                     'operator': '+',
                     'value2': '1'}
        result = self.server.sendRequest(operation)
        self.assertEqual(result['solution'], 2, "Should be 2")

    # TEST 2:
    def test_addition2(self):
        operation = {'value1': '4',
                     'operator': '+',
                     'value2': '2'}
        result = self.server.sendRequest(operation)
        self.assertEqual(result['solution'], 6, "Should be 6")

    def test_addition3(self):
        operation = {'value1': '4.5',
                     'operator': '+',
                     'value2': '3'}
        result = self.server.sendRequest(operation)
        self.assertEqual(result['solution'], 7.5, "Should be 7.5")

    # Different tests made to the subtraction operation
    # TEST 1:
    def test_subtraction1(self):
        operation = {'value1': '1',
                     'operator': '-',
                     'value2': '1'}
        result = self.server.sendRequest(operation)
        self.assertEqual(result['solution'], 0, "Should be 0")

    # TEST 2:
    def test_subtraction2(self):
        operation = {'value1': '4',
                     'operator': '-',
                     'value2': '2'}
        result = self.server.sendRequest(operation)
        self.assertEqual(result['solution'], 2, "Should be 2")

    def test_subtraction3(self):
        operation = {'value1': '4.5',
                     'operator': '-',
                     'value2': '5'}
        result = self.server.sendRequest(operation)
        self.assertEqual(result['solution'], -0.5, "Should be -0.5")

    # Different tests made to the multiplication operation
    # TEST 1:
    def test_multiplication1(self):
        operation = {'value1': '1',
                     'operator': '*',
                     'value2': '-1'}
        result = self.server.sendRequest(operation)
        self.assertEqual(result['solution'], -1, "Should be -1")

    # TEST 2:
    def test_multiplication2(self):
        operation = {'value1': '4',
                     'operator': '*',
                     'value2': '2'}
        result = self.server.sendRequest(operation)
        self.assertEqual(result['solution'], 8, "Should be 8")

    def test_multiplication3(self):
        operation = {'value1': '4.5',
                     'operator': '*',
                     'value2': '3'}
        result = self.server.sendRequest(operation)
        self.assertEqual(result['solution'], 13.5, "Should be 13.5")

    # Different tests made to the division operation
    # TEST 1:
    def test_division1(self):
        operation = {'value1': '1',
                     'operator': '/',
                     'value2': '-1'}
        result = self.server.sendRequest(operation)
        self.assertEqual(result['solution'], -1, "Should be -1")

    # TEST 2:
    def test_division2(self):
        operation = {'value1': '4',
                     'operator': '/',
                     'value2': '2'}
        result = self.server.sendRequest(operation)
        self.assertEqual(result['solution'], 2, "Should be 2")

    def test_dvision3(self):
        operation = {'value1': '4.5',
                     'operator': '/',
                     'value2': '3'}
        result = self.server.sendRequest(operation)
        self.assertEqual(result['solution'], 1.5, "Should be 1.5")


if __name__ == '__main__':
    unittest.main()

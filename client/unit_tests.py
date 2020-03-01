import unittest
import serverConnection as s


class TestSum(unittest.TestCase):

    def setUp(self):
        self.server = s.ServerConnection('http://127.0.0.1:5000/')

    # Different tests made to the sum operation
    # TEST 1:
    def test_sum1(self):

        operation = {'value1': '1',
                     'operator': '+',
                     'value2': '1'}
        result = self.server.sendRequest(operation)
        self.assertEqual(result['solution'], 2, "Should be 2")

    # TEST 2:
    def test_sum2(self):
        operation = {'value1': '2',
                     'operator': '+',
                     'value2': '4'}
        result = self.server.sendRequest(operation)
        self.assertEqual(result['solution'], 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()

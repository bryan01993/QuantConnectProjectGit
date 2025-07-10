import ast
import unittest
from PropietaryCode.decorators import FunctionLogger


class DummyAlgo:
    def __init__(self):
        self.messages = []

    def Debug(self, msg):
        self.messages.append(msg)

    def Error(self, msg):
        self.messages.append(msg)


class TestFunctionLogger(unittest.TestCase):
    def test_truncate_list_and_dict(self):
        algo = DummyAlgo()
        logger = FunctionLogger(algo)
        long_list = list(range(20))
        long_dict = {i: i for i in range(15)}
        self.assertEqual(len(logger._truncate(long_list)), 11)
        self.assertEqual(len(logger._truncate(long_dict)), 11)

    def test_logging_truncates_values(self):
        algo = DummyAlgo()
        logger = FunctionLogger(algo)

        @logger.log
        def example(a):
            return list(range(15))

        example(list(range(20)))
        self.assertTrue(algo.messages)
        data = ast.literal_eval(algo.messages[0])
        self.assertEqual(len(data['args']['a']), 11)
        self.assertEqual(len(data['result']), 11)


if __name__ == '__main__':
    unittest.main()

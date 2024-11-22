import unittest

def sum(a, b):
    """Calculates the sum of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """

    return a + b

def string_length(s):
    """Calculates the length of a string.

    Args:
        s: The input string.

    Returns:
        The length of the string.
    """

    return len(s)

def add_to_dict(d, key, value):
    """Adds a value to a dictionary key if it exists, otherwise creates a new key-value pair.

    Args:
        d: The dictionary.
        key: The key to add or modify.
        value: The value to add or assign.
    """

    d[key] = value

class TestFunctions(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sum(-1, 1), 0)

    def test_string_length(self):
        self.assertEqual(string_length("hello"), 5)
        self.assertEqual(string_length(""), 0)

    def test_add_to_dict(self):
        d = {}
        add_to_dict(d, "a", 1)
        self.assertEqual(d, {"a": 1})
        add_to_dict(d, "a", 2)
        self.assertEqual(d, {"a": 2})

if __name__ == "__main__":
    unittest.main()
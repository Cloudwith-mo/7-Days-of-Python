# import pdb

# def add_numbers(x, y):
#     result = x + y
#     pdb.set_trace() # Start the debugger at this point in the code
#     return result

# result = add_numbers(2,3)
# print(result)


import unittest

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(6))
        
if __name__ == '__main__':
    unittest.main()
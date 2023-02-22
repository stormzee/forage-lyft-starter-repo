import unittest
import os
import sys
from 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


class TestTyre(unittest.TestCase):
    def test_tyre_needs_service(self):
        # create a tyre_type class
        # tyre needs servicing if the array consist of a value greater than 0.4
        
        tyre_array = [0, 0.2, 0.03, 0.46]
        tyre = tyre_type.TyreType(tyre_array)
        self.assertTrue(tyre.needs_service())
        
        
        
if __name__ == "__main__":
    unittest.main()
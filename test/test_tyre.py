import unittest
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from tyre import Carrigan_tyre, Octoprime_tyre





class TestCarriganTyre(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        tyre_wear_array = [0, 0.2, 0.03, 0.98]
        tyre = Carrigan_tyre.CarriganTyre(tyre_wear_array)
        self.assertTrue(tyre.needs_service())
        
        
    def test_tyre_should_not_be_serviced(self):
        tyre_wear_array = [0, 0.2, 0.03, 0.4]
        tyre = Carrigan_tyre.CarriganTyre(tyre_wear_array)
        self.assertFalse(tyre.needs_service())
        
        
        
        
class TestOctoprimeTyre(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        tyre_wear_array = [0.95, 0.95, 0.98, 0.98]
        tyre = Octoprime_tyre.OctoprimeTyre(tyre_wear_array)
        self.assertTrue(tyre.needs_service())
    
    
    def test_tyre_should_not_be_serviced(self):
        tyre_wear_array = [0, 0.2, 0.03, 0.98]
        tyre = Octoprime_tyre.OctoprimeTyre(tyre_wear_array)
        self.assertFalse(tyre.needs_service())
        
        
        
if __name__ == "__main__":
    unittest.main()
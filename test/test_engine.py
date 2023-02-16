import unittest
from datetime import datetime

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from engine import capulet_engine, sternman_engine, willoughby_engine


class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        current_mileage = 90000
        last_service_mileage = 0
        car_engine = capulet_engine.CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car_engine.needs_service())
    
    
    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        car_engine = capulet_engine.CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car_engine.needs_service())
    
    
    
class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        warning_light_is_on = True
        car_engine = sternman_engine.SternmanEngine(last_service_date, warning_light_is_on)
        self.assertTrue(car_engine.needs_service())
    
    
    
    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        warning_light_is_on = False
        car_engine = sternman_engine.SternmanEngine(last_service_date, warning_light_is_on)
        self.assertFalse(car_engine.needs_service())
    
    

class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        current_mileage = 110000
        last_service_mileage = 100
        car_engine = willoughby_engine.WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car_engine.needs_service())
    
    
    
    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        current_mileage = 2000
        last_service_mileage = 0
        car_engine = willoughby_engine.WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car_engine.needs_service())
    
    
    



if __name__ == '__main__':
    unittest.main()
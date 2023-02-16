import unittest
from datetime import datetime

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from carfactory  import CarFactory as factory
from battery import spindlerbattery, nubbinbattery
from engine import capulet_engine, sternman_engine, willoughby_engine

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        car_battery = spindlerbattery.SpindlerBattery(last_service_date, current_date)
        self.assertTrue(car_battery.needs_service())
    
    
#     def test_battery_should_not_be_serviced(last_service_date, current_date):
#         current_date = datetime.today().date()
#         last_service_date = current_date.replace(year=current_date.year - 1)
#         pass
    
    
    
class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        car_battery = nubbinbattery.NubbinBattery(last_service_date, current_date)
        self.assertTrue(car_battery.needs_service())
    
    
    
#     def battery_should_not_be_serviced(last_service_date, current_date):
#         current_date = datetime.today().date()
#         last_service_date = current_date.replace(year=current_date.year - 1)
#         pass
    
    
    



if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()

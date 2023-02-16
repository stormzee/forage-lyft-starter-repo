
from battery import *
import unittest
from datetime import datetime
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)





class TestSpindler(unittest.TestCase):
    def battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        
        car_battery = battery.spindlerbattery.SpindlerBattery(last_service_date, current_date)
        self.assertTrue(car_battery.needs_service())
    
    
#     def battery_should_not_be_serviced(last_service_date, current_date):
#         current_date = datetime.today().date()
#         last_service_date = current_date.replace(year=current_date.year - 1)
#         pass
    
    
    
class TestNubbin(unittest.TestCase):
    def battery_should_be_serviced(last_service_date, current_date):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        car_battery = battery.nubbinbattery.NubbinBattery(last_service_date, current_date)
        self.assertTrue(car_battery.needs_service())
    
    
    
#     def battery_should_not_be_serviced(last_service_date, current_date):
#         current_date = datetime.today().date()
#         last_service_date = current_date.replace(year=current_date.year - 1)
#         pass
    
    
    



if __name__ == '__main__':
    unittest.main()
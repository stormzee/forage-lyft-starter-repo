
import unittest
from datetime import datetime
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# sys.path.append("..\forage-lyft-starter-repo")

# import battery
import battery.spindlerbattery as sp



class TestSpindler(unittest.TestCase):
    def battery_should_be_serviced(self, last_service_date, current_date):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 5)
        
        battery = sp.SpindlerBattery.SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())
    
    
#     def battery_should_not_be_serviced(last_service_date, current_date):
#         current_date = datetime.today().date()
#         last_service_date = current_date.replace(year=current_date.year - 1)
#         pass
    
    
    
# class TestSpindler(unittest.TestCase):
#     def battery_should_be_serviced(last_service_date, current_date):
#         current_date = datetime.today().date()
#         last_service_date = current_date.replace(year=current_date.year - 1)
#         pass
    
    
#     def battery_should_not_be_serviced(last_service_date, current_date):
#         current_date = datetime.today().date()
#         last_service_date = current_date.replace(year=current_date.year - 1)
#         pass
    
    
    



if __name__ == '__main__':
    unittest.main()